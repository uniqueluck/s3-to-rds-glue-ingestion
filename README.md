🚀 Data Ingestion from S3 to RDS with Fallback to Glue

This project reads a CSV from an S3 bucket, uploads it to an RDS MySQL database, and falls back to AWS Glue if the RDS push fails. The entire workflow is automated using a Python script and packaged in a Docker container for portability.

🔄 Data Flow Architecture

<p align="center">
  <img src="images/Data Flow Diagram.png" alt="Data Flow Diagram" width="700"/>
</p>


1. Read CSV file from Amazon S3

2. Attempt to push to Amazon RDS (MySQL-compatible)

3. If the RDS connection/upload fails:

Automatically fall back to AWS Glue Data Catalog

Register the dataset and schema based on S3 file



🐍 Python Script Logic

<p align="center">
  <img src="images/Python Code Screenshot.png" alt="Python Code Screenshot" width="700"/>
</p>


The script:

Uses boto3 to connect to S3 and download a CSV

Parses the CSV using pandas

Uploads it to RDS via SQLAlchemy

If RDS fails, uses boto3 to create a table in AWS Glue



📁 AWS Glue Fallback

<p align="center">
  <img src="images/Glue.png" alt="Glue Table Screenshot" width="700"/>
</p>

<p align="center">
  <img src="images/Glue_table.png" alt="Glue Table Screenshot" width="700"/>
</p>

<p align="center">
  <img src="images/Glue Table Screenshot.png" alt="Glue Table Screenshot" width="700"/>
</p>

If the RDS upload fails, the script registers the CSV file in the Glue Data Catalog:

<p align="center">
  <img src="images/RDS_database.png" alt="RDS_database" width="700"/>
</p>

<p align="center">
  <img src="images/Docker_log.png" alt="Docker_log" width="700"/>
</p>




🐳 Docker Setup
<p align="center">
  <img src="images/tree-diagram.png.png" alt="tree" width="700"/>
</p>



The project is containerized using Docker:


docker build -t s3-to-rds-fallback .


Run the container with required environment variables:


<p align="center">
  <img src="images/docker_run.png" alt="Docker_run" width="700"/>
</p>



✅ Final Output Logs

<p align="center">
  <img src="images/Docker_log.png" alt="Docker_log" width="700"/>
</p>



🌟 Why Use This Project?

This project demonstrates how to build a resilient, cloud-native data ingestion pipeline using real-world AWS services. It showcases key DevOps and cloud engineering skills, including:

✅ Automated ingestion from S3 to RDS

✅ Error handling with fallback to AWS Glue

✅ Dockerized deployment for portability

✅ Secure AWS integration using environment variables

✅ Clean code and logging

✅ Benefits
Feature Benefit


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


