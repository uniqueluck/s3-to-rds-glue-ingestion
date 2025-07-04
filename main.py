"""
🚀 Data Ingestion Script

This script performs the following steps:

1️⃣ Uses boto3 to connect to S3 and download a CSV file.  
2️⃣ Parses the CSV using pandas.  
3️⃣ Uploads the data to Amazon RDS (MySQL) using SQLAlchemy.  
4️⃣ If RDS upload fails, automatically falls back to AWS Glue:  
    - Registers the dataset and schema in Glue Data Catalog.

Tools & Libraries:
- boto3
- pandas
- SQLAlchemy

"""


import os
import boto3
import pandas as pd
import pymysql
from sqlalchemy import create_engine

def download_csv_from_s3(bucket, key, local_file):
    s3 = boto3.client('s3')
    s3.download_file(bucket, key, local_file)
    print(f"Downloaded {key} from {bucket}")

def upload_to_rds(df):
    try:
        engine = create_engine(
            f"mysql+pymysql://{os.environ['RDS_USER']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOST']}/{os.environ['RDS_DB']}"
        )
        df.to_sql(os.environ['RDS_TABLE'], con=engine, if_exists='replace', index=False)
        print("Upload to RDS successful.")
        return True
    except Exception as e:
        print("RDS upload failed:", e)
        return False

def register_in_glue(df):
    glue = boto3.client('glue')
    s3_path = f"s3://{os.environ['S3_BUCKET']}/{os.environ['S3_KEY']}"
    try:
        glue.create_table(
            DatabaseName=os.environ['GLUE_DB'],
            TableInput={
                'Name': os.environ['GLUE_TABLE'],
                'StorageDescriptor': {
                    'Columns': [{'Name': col, 'Type': 'string'} for col in df.columns],
                    'Location': s3_path,
                    'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
                    'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                    'SerdeInfo': {
                        'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
                        'Parameters': {'field.delim': ','}
                    }
                },
                'TableType': 'EXTERNAL_TABLE'
            }
        )
        print("Fallback to Glue successful.")
    except glue.exceptions.AlreadyExistsException:
        print("Glue table already exists. Skipping.")

def main():
    local_file = '/tmp/data.csv'
    download_csv_from_s3(os.environ['S3_BUCKET'], os.environ['S3_KEY'], local_file)
    df = pd.read_csv(local_file)

    if not upload_to_rds(df):
        register_in_glue(df)

if __name__ == "__main__":
    main()
