# 🚀 Deploying a Highly Available 3-Tier Web Architecture on AWS with Terraform & Ansible

---

## 📖 Table of Contents
1. [Project Overview](#project-overview)
2. [Why This Project is Important](#why-this-project-is-important)
3. [What You Will Learn](#what-you-will-learn)
4. [Real-World Use Cases](#real-world-use-cases)
5. [Step-by-Step Implementation](#step-by-step-implementation)
6. [Screenshots Summary](#screenshots-summary)
7. [GitHub Repository](#github-repository)
8. [Conclusion](#conclusion)

---

## 📌 Project Overview
This beginner-friendly project shows how to deploy a **highly available 3-tier architecture** on AWS using **Terraform** and **Ansible**.


---

## 🎯 Why This Project is Important
- Learn **real-world AWS infrastructure design**
- Apply **Infrastructure as Code (IaC)** concepts
- Automate multi-tier app deployments

---

## 📚 What You Will Learn
✅ Provision AWS resources using Terraform modules  
✅ Configure servers with Ansible  
✅ Deploy and test a full 3-tier architecture

---

## 🌍 Real-World Use Cases
- Hosting scalable web applications
- Automating deployments in DevOps pipelines
- Multi-tier architecture deployments

---

## 🛠 Step-by-Step Implementation

### 🌐 Step 1: Launch EC2 for Terraform & Ansible
Login to AWS Console → Search for “EC2” → Launch instance → Amazon Linux 2 → t2.micro → Create key pair → Launch.

<p align="center">
  <img src="Screenshots/01-Launch-EC2.png" alt="Launch EC2" width="900"/>
</p>
📖 *EC2 instance launch configuration.*

---

### ⚙️ Step 2: Install Terraform & Ansible
SSH into EC2 and run:
```bash
sudo yum update -y
sudo yum install -y wget unzip
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/
sudo amazon-linux-extras install ansible2 -y
```



---

### 📦 Step 3: Write Terraform Code
Folder structure:
```
terraform-3tier-project/
├── main.tf
├── variables.tf
├── outputs.tf
├── provider.tf
├── modules/
│   ├── vpc/
│   ├── ec2/
│   └── rds/
```
<p align="center">
  <img src="images/03-Terraform-Structure.png" alt="Terraform Structure" width="900"/>
</p>
📖 *Terraform folder and files overview.*

---

### 🚀 Step 4: Apply Terraform to Provision Infrastructure
```bash
cd terraform-3tier-project
terraform init
terraform plan
terraform apply
```
<p align="center">
  <img src="terraform.png" alt="Terraform Apply" width="900"/>
</p>
📖 *Terraform provisioning AWS resources.*

---

### 📝 Step 5: Configure Servers with Ansible
Run:
```bash
cd ansible-3tier-setup
ansible-playbook -i inventory site.yml
```
<p align="center">
  <img src="Screenshots/5_ansible_playbook_run.png" alt="Ansible Playbook" width="900"/>
</p>
📖 *Ansible playbook applying configurations.*

---

### ✅ Step 6: Verify Setup
- Visit the web app URL → Submit registration form
- Check RDS database for new entries
<p align="center">
  <img src="Screenshots/1_web_registration_form.png" alt="Web App" width="900"/>
</p>

<p align="center">
  <img src="Screenshots/2_form_submission_success.png" alt="Web App" width="900"/>
</p>
📖 *Web app registration form.*

<p align="center">
  <img src="Screenshots/3_rds_database_entr.png" alt="RDS Database" width="900"/>
</p>
📖 *Data entries visible in RDS database.*

---

## 📸 Screenshots Summary
| Step                     | Screenshot                                  | Description                             |
|--------------------------|----------------------------------------------|-----------------------------------------|
| Launch EC2               | images/01-Launch-EC2.png                    | EC2 instance launch                     |
| Install Terraform/Ansible| images/02-Install-Terraform-Ansible.png      | Terraform & Ansible installation        |
| Terraform Files          | images/03-Terraform-Structure.png           | Terraform folder structure              |
| Terraform Apply          | images/04-Terraform-Apply.png               | Terraform apply result                  |
| Ansible Playbook         | images/05-Ansible-Playbook.png              | Running Ansible playbook                |
| Web App                  | images/06-Web-App.png                       | Registration form running               |
| RDS Database             | images/07-RDS-Entries.png                   | Data entries in RDS                     |

---

## 🔗 GitHub Repository
All code files are available here: [GitHub Repo](https://github.com/uniqueluck/3tier-aws-project)

---

## 🎉 Conclusion
This documentation helps even beginners deploy a 3-tier AWS architecture using Terraform & Ansible with step-by-step guidance and screenshots.
