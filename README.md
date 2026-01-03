# Medical ChatBot Using Generative AI

[![Python](https://img.shields.io/badge/Python-3.10.11-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/aliahmad552/medical_chatbot_generative_ai?style=social)](https://github.com/aliahmad552/medical_chatbot_generative_ai/stargazers)

**A RAG-based Generative AI Medical Chatbot with Knowledge Base Integration, FastAPI Backend, and Web Frontend.**

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture & Flow](#architecture--flow)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Author](#author)
- [License](#license)

---

## Overview

This project is a **Medical Chatbot** powered by **Generative AI** using a Retrieval-Augmented Generation (RAG) approach. It can answer medical queries by retrieving relevant knowledge from your uploaded documents (PDFs or directories) and generating accurate, context-aware responses using **OpenAI** language models.  

The chatbot is fully **dockerized** and deployed on **AWS EC2**, with **CI/CD integration using ECR**, enabling seamless updates and scalable deployment.

---

## Features

- **RAG-based AI**: Combines retrieval from knowledge base and generation using OpenAI LLM.  
- **Knowledge Base Loader**:
  - Directory loader for structured knowledge.
  - PDF loader for medical documents.
- **Recursive Character Text Splitter**: Handles large documents efficiently.  
- **Vector Database**: Pinecone integration for fast semantic search.  
- **Embeddings**: Sentence Transformers for high-quality text embeddings.  
- **Backend**: FastAPI for API endpoints.  
- **Frontend**: Interactive HTML/CSS UI for chat interaction.  
- **Deployment**:
  - Dockerized application.
  - AWS EC2 deployment.
  - CI/CD using AWS ECR.

---

## Architecture & Flow

```mermaid
flowchart LR
    A[User] --> B[Frontend UI (HTML/CSS)]
    B --> C[FastAPI Backend]
    C --> D[OpenAI LLM]
    C --> E[Pinecone Vector DB]
    E --> F[Knowledge Base (PDFs / Directory)]
    F --> E
    D --> B
```
### Flow:

- User inputs a query via the frontend.

- FastAPI backend receives the request.

- The query is embedded using Sentence Transformers.

- Pinecone searches the knowledge base for relevant context.

- OpenAI generates a response using the retrieved context.

- Response is sent back to the frontend for the user.

### Installation

Requirements:

- Python 3.10.11

- Docker (for containerized deployment)

- AWS CLI & ECR access (for deployment)

Clone the repository:

```bash
git clone https://github.com/aliahmad552/medical_chatbot_generative_ai.git
cd medical_chatbot_generative_ai
```
### Create virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Run locally:
```bash
uvicorn main:app --reload
```

## Docker deployment:
```bash
docker build -t medical-chatbot .
docker run -p 8000:8000 medical-chatbot
```

AWS Deployment (EC2 + ECR):

# Build Docker image
```bash
docker build -t medical-chatbot .
```


# Deploy container on EC2 instance

Usage

Open your browser and go to: http://localhost:8000

Interact with the chatbot via the web interface.

Backend API endpoints (example):
```bash
POST /chat
{
  "query": "What are the symptoms of diabetes?"
}
```
### Screenshots

Frontend Chat Interface:


## FastAPI Swagger Docs:


(Replace with your actual screenshots in /screenshots directory)

Technologies Used

Backend: Python, FastAPI

Frontend: HTML, CSS

Generative AI: OpenAI LLM, RAG

Knowledge Base: Directory Loader, PDF Loader

Text Processing: Recursive Character Text Splitter

Vector DB: Pinecone

Embeddings: Sentence Transformers

Deployment: Docker, AWS EC2, ECR, CI/CD

## Author

Ali Ahmad

GitHub: https://github.com/aliahmad552

LinkedIn: https://www.linkedin.com/in/ali-ahmad-dawana

### License

This project is licensed under the MIT License – see the LICENSE
 file for details.