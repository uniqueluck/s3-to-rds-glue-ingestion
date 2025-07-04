# 📗 Beginner Setup Guide: Data Ingestion from S3 to RDS with Fallback to Glue

This guide will take you step by step through setting up your AWS environment, preparing your EC2 instance, and running the Dockerized application.  

It’s designed for **absolute beginners**.

## 📋 Table of Contents
- [🚀 Step 1: Launch EC2 Instance](#-step-1-launch-ec2-instance)
- [🐳 Step 2: Prepare EC2 Environment](#-step-2-prepare-ec2-environment)
- [☁️ Step 3: Set up AWS Services (S3, RDS, Glue)](#-step-3-set-up-aws-services-s3-rds-glue)
- [▶️ Step 4: Run the Project](#-step-4-run-the-project)

## 🚀 Step 1: Launch EC2 Instance

1. Go to [AWS EC2 Console](https://console.aws.amazon.com/ec2/).  
2. Click **Launch Instance**.
3. Select **Amazon Linux 2 AMI**.  
4. Choose `t2.micro` (Free Tier).  
5. Configure Security Group:
   - Allow SSH (port 22), HTTP (80), and MySQL/Aurora (port 3306).
6. Create a key pair (download `my-key.pem`).  
7. Launch.  

📸 *Placeholder Screenshot: images/EC2_Launch.png*  
📸 *Placeholder Screenshot: images/EC2_SecurityGroup.png*

## 🐳 Step 2: Prepare EC2 Environment

SSH into EC2 (from PowerShell on your computer):  
```powershell
ssh -i "C:\Path\To\my-key.pem" ec2-user@<EC2_PUBLIC_IP>
```

### 🛠️ Install Docker
```bash
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
```

📸 *Placeholder Screenshot: images/Docker_Install.png*

### 🛠️ Install Python 3
```bash
sudo yum install python3 -y
```

## ☁️ Step 3: Set up AWS Services (S3, RDS, Glue)

### ✅ S3 Bucket
1. Create bucket `my-s3-data-bucket`.
2. Upload `data.csv`.  
📸 *Placeholder Screenshot: images/S3_Create_Bucket.png*

### ✅ RDS MySQL
1. Create RDS MySQL database `mydb`.
2. Enable public access.
📸 *Placeholder Screenshot: images/RDS_Setup.png*

### ✅ AWS Glue
1. Create Glue Database.
2. Create Crawler for S3 data.
📸 *Placeholder Screenshot: images/Glue_Setup.png*

## ▶️ Step 4: Run the Project

Follow the Docker build and run steps from [README.md](README.md).  

📸 *Placeholder Screenshot: images/Docker_Run.png*
