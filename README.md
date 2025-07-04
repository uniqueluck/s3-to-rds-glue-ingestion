# 🚀 Data Ingestion from S3 to RDS with Fallback to Glue

This project reads a CSV file from **Amazon S3**, uploads it to an **Amazon RDS (MySQL)** database, and automatically falls back to **AWS Glue** if the RDS upload fails. It uses a Python script packaged in a **Docker container** for easy deployment.  

This guide is beginner-friendly and includes links to a full setup tutorial.

## 📦 Table of Contents
- [📸 Architecture](#-architecture)
- [⚙️ Prerequisites](#-prerequisites)
- [🌐 AWS Setup Guide](#-aws-setup-guide)
- [🚀 Setup and Run](#-setup-and-run)
- [🐍 Python Script Logic](#-python-script-logic)
- [🌟 Why Use This Project?](#-why-use-this-project)
- [🙌 Who Should Use This?](#-who-should-use-this)
- [📜 License](#-license)

## 📸 Architecture

<p align="center">
  <img src="images/Data Flow Diagram.png" alt="Data Flow Diagram" width="700"/>
</p>

## ⚙️ Prerequisites

✅ AWS Account ([Sign up here](https://aws.amazon.com/free/))  
✅ PowerShell (comes preinstalled in Windows 10/11)  

## 🌐 AWS Setup Guide

To set up AWS services and prepare your EC2 instance:  

👉 See the full beginner guide: [BeginnerSetup.md](BeginnerSetup.md)  

### ⚙️ Prepare EC2 Environment (Quick Steps)

```bash
# Update and install Docker on Amazon Linux 2
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user

# Install Python 3
sudo yum install python3 -y



## 🚀 Setup and Run

### 🔥 Clone Repository
```powershell
git clone https://github.com/<your-username>/s3-to-rds-fallback.git
cd s3-to-rds-fallback
```

### 🐳 Build Docker Image
```powershell
docker build -t s3-to-rds-fallback .
```

### ▶️ Run Docker Container
```powershell
docker run -e AWS_ACCESS_KEY_ID=XXXXXX `
           -e AWS_SECRET_ACCESS_KEY=XXXXXX `
           -e AWS_DEFAULT_REGION=ap-south-1 `
           -e RDS_HOST=<your-rds-endpoint> `
           -e RDS_PORT=3306 `
           -e RDS_DB=mydb `
           -e RDS_USER=admin `
           -e RDS_PASSWORD=YourPassword123 `
           -e S3_BUCKET_NAME=my-s3-data-bucket `
           -e S3_FILE_KEY=data.csv `
           s3-to-rds-fallback
```

## 🐍 Python Script Logic

<p align="center">
  <img src="images/Python Code Screenshot.png" alt="Python Code Screenshot" width="700"/>
</p>

## 🌟 Why Use This Project?

| Feature                     | Benefit                                        |
|----------------------------|------------------------------------------------|
| 📦 Dockerized App          | Works on any OS with Docker                    |
| 🔁 AWS Glue Fallback        | No data loss if RDS fails                      |
| ☁️ Native AWS Services      | Production-ready pipeline                      |
| 🐍 Python Stack             | Uses boto3, pandas, SQLAlchemy, Docker         |
| 🔒 Secure Configs           | No hardcoded secrets, uses environment vars    |

## 🙌 Who Should Use This?

✅ Beginners exploring AWS  
✅ Students preparing for cloud interviews  
✅ Cloud engineers building fault-tolerant pipelines  

## 📜 License

MIT License. See [LICENSE](LICENSE).  
