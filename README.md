🚀 Data Ingestion from S3 to RDS with Fallback to Glue

This project reads a CSV from an S3 bucket, uploads it to an RDS MySQL database, and falls back to AWS Glue if the RDS push fails. The entire workflow is automated using a Python script and packaged in a Docker container for portability.

🔄 Data Flow Architecture

1. Read CSV file from Amazon S3

2. Attempt to push to Amazon RDS (MySQL-compatible)

3. If the RDS connection/upload fails:

Automatically fall back to AWS Glue Data Catalog

Register the dataset and schema based on S3 file

🐍 Python Script Logic

The script:

Uses boto3 to connect to S3 and download a CSV

Parses the CSV using pandas

Uploads it to RDS via SQLAlchemy

If RDS fails, uses boto3 to create a table in AWS Glue


📁 AWS Glue Fallback

If the RDS upload fails, the script registers the CSV file in the Glue Data Catalog:

🐳 Docker Setup

The project is containerized using Docker:

docker build -t s3-to-rds-fallback .

Run the container with required environment variables:

docker run \
-e AWS_ACCESS_KEY_ID=your-access-key \
-e AWS_SECRET_ACCESS_KEY=your-secret-key \
-e AWS_DEFAULT_REGION=ap-south-1 \
-e S3_BUCKET=my-bucket-data-ingestion \
-e S3_KEY=sample_data.csv \
-e RDS_HOST=your-db.rds.amazonaws.com \
-e RDS_USER=admin \
-e RDS_PASSWORD=admin123 \
-e RDS_DB=ingestion_db \
-e RDS_TABLE=my_table \
-e GLUE_DB=my_glue_db \
-e GLUE_TABLE=my_glue_table \
s3-to-rds-fallback

✅ Final Output Logs

🌟 Why Use This Project?

This project demonstrates how to build a resilient, cloud-native data ingestion pipeline using real-world AWS services. It showcases key DevOps and cloud engineering skills, including:

✅ Automated ingestion from S3 to RDS

✅ Error handling with fallback to AWS Glue

✅ Dockerized deployment for portability

✅ Secure AWS integration using environment variables

✅ Clean code and logging

✅ Benefits

Feature

Benefit

📦 Dockerized App

Easy to run in any environment

🔁 Fallback to AWS Glue

Ensures no data loss even when RDS fails

☁️ Native AWS Services

Production-ready cloud components

🛠️ Real Python Stack

Demonstrates use of boto3, pandas, SQLAlchemy, Docker

🔒 Secure Configs

No hardcoded secrets – all done via environment variables

💡 Who Should Use This Project?

DevOps/Cloud engineers looking to showcase AWS integrations

Students or professionals preparing for AWS interviews

Anyone building fault-tolerant, automated data pipelines

🙌 Thank You!

If you find this project useful, consider ⭐ starring the repo. Feedback and contributions are welcome!

