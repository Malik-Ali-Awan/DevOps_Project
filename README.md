# Quote Saver

A microservices-based web application for saving and viewing quotes, built as a DevOps practice project.

## Project Overview

Quote Saver is a simple web application that allows users to:
- Submit quotes (text strings)
- View a list of all submitted quotes

The application is built using a microservices architecture with the following components:
- Frontend (React.js)
- Backend API (FastAPI)
- Database (PostgreSQL)

## Architecture

### Frontend Service
- Built with React.js
- Provides a form for submitting quotes
- Displays a list of all saved quotes
- Communicates with the backend API

### Quote API Service
- Built with FastAPI
- Exposes REST endpoints:
  - POST /quotes: Save a new quote
  - GET /quotes: Retrieve all quotes
- Connects to PostgreSQL database

### Database Service
- PostgreSQL database
- Stores quotes in a simple table structure

## Prerequisites

- Docker and Docker Compose
- Kubernetes cluster (Minikube or cloud provider)
- Terraform
- Ansible
- kubectl
- ArgoCD

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/quote-saver.git
cd quote-saver
```

2. Start the application using Docker Compose:
```bash
docker-compose up --build
```

3. Access the application:
- Frontend: http://localhost:3000
- API: http://localhost:5000

## Kubernetes Deployment

1. Apply Kubernetes manifests:
```bash
kubectl apply -f k8s/
```

2. Access the application through the configured ingress.

## Infrastructure Setup

1. Initialize Terraform:
```bash
cd terraform
terraform init
terraform apply
```

2. Run Ansible playbooks:
```bash
cd ansible
ansible-playbook setup.yml
```

## CI/CD Pipeline

The project includes GitHub Actions workflows for:
- Building and pushing Docker images
- Running tests
- Deploying to Kubernetes via ArgoCD

## Project Structure

```
quote-saver/
├── frontend/                # React frontend
├── quote-api/              # FastAPI backend
├── postgres-db/            # SQL init scripts
├── k8s/                    # Kubernetes manifests
├── terraform/              # Infrastructure code
├── ansible/                # Ansible playbooks
├── .github/workflows/      # GitHub Actions
├── docker-compose.yml
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License 