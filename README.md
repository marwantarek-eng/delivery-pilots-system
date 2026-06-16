# Delivery Pilots GitOps Automation System

## Overview

Delivery Pilots is a cloud-native microservices platform designed to automate and manage the delivery lifecycle using modern DevOps and GitOps practices.

The primary objective of this project is to demonstrate how a production-oriented delivery platform can be deployed, managed, monitored, and continuously updated through a fully automated infrastructure and deployment pipeline.

The system combines Infrastructure as Code (IaC), Continuous Integration (CI), Continuous Deployment (CD), Kubernetes orchestration, containerization, and observability into a single automated ecosystem.

---

## Architecture Diagram

> Insert the complete architecture diagram here.

<img width="1600" height="872" alt="digram" src="https://github.com/user-attachments/assets/be37b8a7-9a82-49b6-84c6-fbdc493e8b56" />

---

## Project Goals

* Automate infrastructure provisioning on AWS
* Implement CI/CD pipelines for rapid deployments
* Containerize microservices using Docker
* Deploy workloads on Kubernetes (EKS)
* Adopt GitOps methodology using ArgoCD
* Monitor system health and performance
* Provide scalable and reproducible environments

---

## System Components

### Order Service

Responsible for handling customer delivery orders.

Main responsibilities:

* Create new delivery orders
* Store order information
* Expose APIs for order management
* Communicate with other platform services

---

### Pilot Service

Responsible for managing delivery pilots.

Main responsibilities:

* Pilot registration
* Pilot assignment
* Delivery status tracking
* Service communication

---

## Technology Stack

### Cloud Platform

* AWS EC2
* AWS ECR
* AWS EKS
* AWS VPC

### DevOps & Automation

* Terraform
* Jenkins
* Docker
* Kubernetes
* ArgoCD

### Monitoring & Observability

* Prometheus
* Grafana

### Source Control

* Git
* GitHub

---

# Infrastructure Provisioning

Infrastructure provisioning is fully automated using Terraform.

Provisioned resources include:

* Virtual Private Cloud (VPC)
* Public and Private Subnets
* Internet Gateway
* Route Tables
* Security Groups
* Amazon EKS Cluster
* Worker Nodes

This approach ensures repeatability, consistency, and version-controlled infrastructure management.

---

# Continuous Integration Pipeline

Jenkins is responsible for automating the CI process.

Pipeline workflow:

1. Pull source code from GitHub
2. Build Docker images
3. Tag application versions
4. Push images to Amazon ECR
5. Update deployment manifests

---


# Container Registry

Docker images are stored in Amazon Elastic Container Registry (ECR).

Benefits:

* Secure image storage
* Version control for application releases
* Easy integration with EKS deployments

---

## Amazon ECR

<img width="1576" height="695" alt="ECR" src="https://github.com/user-attachments/assets/097e8428-65ee-4bf6-85ce-2b46e6ccdec8" />

---

# Kubernetes Deployment

Applications are deployed on Amazon EKS.

Features:

* High availability
* Container orchestration
* Self-healing workloads
* Horizontal scalability

Deployment resources:

* Deployments
* Services
* Namespaces
* Ingress

---


# GitOps with ArgoCD

ArgoCD continuously monitors the Git repository and synchronizes the Kubernetes cluster with the desired state stored in Git.

Benefits:

* Automated deployments
* Reduced manual intervention
* Consistent cluster state
* Easy rollback capabilities

---

## ArgoCD Dashboard

<img width="1576" height="695" alt="ARGO" src="https://github.com/user-attachments/assets/3f94d159-1776-461b-94a2-4ef551dd59bb" />

---

# Monitoring and Observability

Prometheus collects metrics from Kubernetes workloads and infrastructure components.

Grafana visualizes those metrics through dashboards, providing operational insights into system performance.

Monitored metrics include:

* Pod health
* CPU utilization
* Memory utilization
* Cluster performance
* Service availability

---

## Prometheus

<img width="1554" height="2141" alt="Prom" src="https://github.com/user-attachments/assets/70f2783d-f553-47d5-a237-208cd183da3c" />

---

## Grafana Dashboard

<img width="1596" height="734" alt="Grafana" src="https://github.com/user-attachments/assets/d219f6e3-8879-4004-a86d-f1971faf2e5e" />

---

# Challenges Faced

### Infrastructure Consistency

Maintaining consistent environments across deployments was a challenge.

**Solution**

Infrastructure provisioning was standardized using Terraform, ensuring repeatable deployments.

---

### Deployment Automation

Manual deployment steps increased operational overhead.

**Solution**

Jenkins and ArgoCD were integrated to create a fully automated deployment workflow.

---

### Observability

Monitoring distributed services required centralized metrics collection.

**Solution**

Prometheus and Grafana were implemented to provide real-time visibility into system health.

---

# CI/CD Workflow

Developer
→ GitHub
→ Jenkins Pipeline
→ Docker Build
→ Amazon ECR
→ GitOps Repository Update
→ ArgoCD
→ Amazon EKS
→ Running Microservices

---

# Future Enhancements

* Service Mesh Integration
* Horizontal Pod Autoscaling
* Centralized Logging using ELK Stack
* Multi-Environment Deployment Strategy
* Automated Security Scanning

---

# Contributors

### Marwan Tarek Ali

DevOps Engineer

### Ziad Ibrahim

DevOps Engineer

---

# Repository Structure

```text
delivery-pilots-system/
│
├── Jenkinsfile
│
├── services/
│   ├── order-svc/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   └── requirements.txt
│   │   ├── Dockerfile
│   │   └── Jenkinsfile
│   │
│   └── pilot-svc/
│       ├── app/
│       │   ├── main.py
│       │   └── requirements.txt
│       ├── Dockerfile
│       └── Jenkinsfile
│
├── terraform/
│   ├── providers.tf
│   ├── variables.tf
│   ├── vpc.tf
│   ├── eks.tf
│   └── ecr.tf
│
├── k8s-manifests/
│   ├── order-svc.yaml
│   ├── pilot-svc.yaml
│   └── ingress.yaml
│
└── README.md
```

---

Built using modern DevOps, Cloud Native, and GitOps practices.
