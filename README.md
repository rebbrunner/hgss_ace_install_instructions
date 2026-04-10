# HGSS/Platinum ACE Installation Guide Website

author: Rebecca Bruner<br>
date: 28 March 2026

## Description
A website for hosting instructions on how to install HGSS and Platinum ACE exploits

## Installation Requirements

- Docker
- Kube cluster
- Configure a secrets called `environment` with two key value pairs:
  - **DB_URL**: Postgres connection string (make sure to encode password special characters)
  - **POSTGRES_PASSWORD**: Raw string password

### Install procedure

1. Build docker file (pre-built artifact profided for convenience)
2. Create `environment` secret
3. Install helm chart
