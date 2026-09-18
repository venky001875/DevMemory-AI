# 🧠 DevMemory AI – Project-Aware GenAI Developer Memory & Troubleshooting Assistant

A developer-focused **AI memory and troubleshooting assistant** that connects to a real local engineering project, records terminal commands, errors, solutions, and development activity, and eventually uses **LLMs, embeddings, semantic search, RAG, and Zep memory** to provide project-aware assistance.

The main goal is simple:

> **"Have I faced this problem before?"**

DevMemory AI maintains project-specific engineering history so developers can retrieve previous commands, errors, fixes, notes, and AI-generated explanations.

---

## 🎯 Core Idea

DevMemory AI connects a developer's **real local project folder** with a backend and AI memory system.

```text
👨‍💻 Developer
      |
      | Works inside project
      v
📁 Real Local Project Folder
      |
      v
💻 Terminal
      |
      v
⚙️ DevMemory CLI / Agent
      |
      | HTTPS
      v
🚀 FastAPI Backend
      |
      +-------------------+
      |                   |
      v                   v
🗄️ PostgreSQL        🤖 AI Services
                          |
              +-----------+-----------+
              |           |           |
              v           v           v
           OpenAI     Embeddings     Zep
              |           |           |
              +-----------+-----------+
                          |
                          v
                  🖥️ React Dashboard
```

---

# 🏗 3-Layer Application Architecture

| **Layer**  | **Component** | **Technology**            | **Purpose**                    |
| ---------- | ------------- | ------------------------- | ------------------------------ |
| 🟢 Layer 1 | Frontend      | React + Vite              | Developer dashboard            |
| 🟡 Layer 2 | Backend       | Python + FastAPI          | REST API and application logic |
| 🔵 Layer 3 | Data & AI     | PostgreSQL + OpenAI + Zep | Persistent data and AI memory  |

---

# 📋 Development Phases

## 🏗 PHASE 0 – Project Planning & Environment

**Objective:** Establish the project structure and development environment.

* Project architecture designed
* Repository structure created
* Git initialized
* `.gitignore` configured
* Development tools verified
* MVP boundaries defined

**Complete:** ✅ Project foundation established

---

## ⚡ PHASE 1 – FastAPI Backend Fundamentals

**Objective:** Build and understand the FastAPI backend before introducing the database.

### Task 1 – FastAPI Foundation

Implemented:

```text
GET /
GET /health
```

* FastAPI application
* Uvicorn development server
* Basic application structure

**Complete:** ✅

### Task 2 – Backend Configuration

Implemented:

```text
backend/app/core/config.py
```

* Separate configuration from application setup
* Prepared structure for future environment configuration

**Complete:** ✅

### Task 3 – FastAPI Routers

Created:

```text
backend/app/routers/
└── health.py
```

Implemented router-based endpoint organization.

**Complete:** ✅

### Task 4 – Pydantic Response Models

Created:

```text
backend/app/schemas/health.py
```

Implemented validated response models using Pydantic.

**Complete:** ✅

### Task 5 – Pydantic Request Models

Implemented request-body validation using Pydantic models.

Example:

```text
JSON Request
     ↓
Pydantic Model
     ↓
Validation
     ↓
FastAPI Endpoint
```

**Complete:** ✅

### Task 6 – HTTP Methods

Implemented REST API demonstrations for:

```text
GET
POST
PUT
PATCH
DELETE
```

**Complete:** ✅

### Task 7 – Projects API

Implemented the first real DevMemory AI domain feature.

Project structure:

```text
Project
├── id
├── name
└── path
```

Current storage:

```text
Python In-Memory Dictionary
```

Endpoints:

```text
POST  /projects/
GET   /projects/
GET   /projects/{project_id}
```

**Complete:** ✅

### Task 8 – Project Update & Delete

Adding:

```text
PATCH  /projects/{project_id}
DELETE /projects/{project_id}
```

PATCH supports partial updates of:

```text
name
path
```

DELETE removes the project from temporary storage.

**Status:** 🔄 In Progress

---

# 🗄 PHASE 2 – PostgreSQL & Database

**Objective:** Replace temporary in-memory storage with persistent database storage.

Planned technologies:

* PostgreSQL
* SQLAlchemy
* Alembic
* Database models
* Database migrations
* Relationships
* CRUD services

Architecture:

```text
FastAPI
   |
   v
SQLAlchemy
   |
   v
PostgreSQL
```

**Status:** ⏳ Planned

---

# 📁 PHASE 3 – Project Management

**Objective:** Build complete project management around real engineering projects.

Planned features:

* Create projects
* Update projects
* Delete projects
* Project details
* Project membership
* Project-specific history
* Project notes
* Project tags

The project will eventually represent a **real local project folder**.

Example:

```text
Project Name:
DevMemory AI

Local Path:
C:\DevMemoryAI
```

**Status:** ⏳ Planned

---

# 💻 PHASE 4 – DevMemory CLI MVP

**Objective:** Create the local CLI that connects DevMemory AI with the developer's actual project.

Planned commands:

```bash
devmemory init
devmemory register
devmemory run
devmemory status
devmemory history
devmemory explain
```

Architecture:

```text
Developer Terminal
       |
       v
DevMemory CLI
       |
       v
Execute Command
       |
       v
Capture Result
       |
       v
Send to FastAPI
```

The CLI will capture:

* Command
* Current working directory
* Terminal type
* stdout
* stderr
* Exit code
* Status
* Timestamp
* Git branch
* Category

**Status:** ⏳ Planned

---

# 🧾 PHASE 5 – Command & Error Tracking

**Objective:** Build persistent engineering history.

Example:

```text
Project
   |
   └── Command
          |
          ├── stdout
          ├── stderr
          ├── exit code
          ├── status
          └── timestamp
```

Failed commands will create error records.

Example:

```text
Command:
docker compose up

Status:
FAILED

Error:
Port 8000 is already allocated
```

The system will store the error and related troubleshooting information.

**Status:** ⏳ Planned

---

# 🖥 PHASE 6 – React Developer Dashboard

**Objective:** Build a frontend dashboard for project and engineering history.

Planned interface:

```text
┌─────────────────────────────────────────┐
│             DevMemory AI                │
├───────────────┬─────────────────────────┤
│ Projects      │ Project Details         │
│               │                         │
│ DevMemory     │ Commands                │
│ FastAPI       │ Errors                  │
│ AWS Project   │ Solutions               │
│               │ Notes                   │
│               │ AI Analysis             │
└───────────────┴─────────────────────────┘
```

Technologies:

* React
* Vite
* Axios
* React Router
* Tailwind CSS

**Status:** ⏳ Planned

---

# 🔗 PHASE 7 – Frontend + Backend Integration

**Objective:** Connect the React dashboard with the FastAPI APIs.

Architecture:

```text
React
  |
  | Axios
  v
FastAPI
  |
  v
PostgreSQL
```

Planned functionality:

* Create projects from UI
* View projects
* Update projects
* Delete projects
* View commands
* View errors
* View solutions

**Status:** ⏳ Planned

---

# 🤖 PHASE 8 – OpenAI Integration

**Objective:** Introduce AI-powered engineering assistance.

Flow:

```text
Developer Error
      |
      v
FastAPI
      |
      v
OpenAI
      |
      v
AI Analysis
      |
      +── Explanation
      +── Possible Causes
      +── Suggested Solution
```

The AI will help explain engineering errors and provide troubleshooting guidance.

**Status:** ⏳ Planned

---

# 🧮 PHASE 9 – Embeddings & Semantic Search

**Objective:** Search engineering history based on meaning instead of exact keywords.

Example:

Previous error:

```text
Docker port 8000 is already allocated
```

Developer asks:

```text
Why can't my backend start because of a port issue?
```

Semantic search should identify the related previous error even when the wording is different.

Architecture:

```text
Engineering Memory
       |
       v
   Embeddings
       |
       v
Semantic Search
       |
       v
Relevant Memories
```

**Status:** ⏳ Planned

---

# 🧠 PHASE 10 – Zep Memory

**Objective:** Introduce long-term project-aware memory.

Planned memory:

```text
Project
   |
   ├── Commands
   ├── Errors
   ├── Solutions
   ├── Notes
   └── AI Conversations
```

Zep will be explored as part of the long-term memory architecture.

**Status:** ⏳ Planned

---

# 🔎 PHASE 11 – RAG Pipeline

**Objective:** Combine project memory with LLM reasoning.

Architecture:

```text
Developer Question
        |
        v
     Embedding
        |
        v
 Semantic Retrieval
        |
        v
Relevant Project Memories
        |
        v
      Context
        |
        v
       LLM
        |
        v
Project-Aware Answer
```

This allows DevMemory AI to answer questions using the developer's own previous engineering experience.

**Status:** ⏳ Planned

---

# ✅ PHASE 12 – Solution Verification

**Objective:** Track whether suggested solutions actually worked.

Flow:

```text
Error
  |
  v
AI Suggested Solution
  |
  v
Developer Attempts Solution
  |
  v
Result
  |
  +── SUCCESS
  |
  └── FAILED
```

Verified solutions can become valuable project memories.

**Status:** ⏳ Planned

---

# 🖥️ PHASE 13 – Advanced CLI

**Objective:** Expand the CLI from manual command execution to richer developer workflow integration.

Planned capabilities:

* Command history
* Error detection
* Git information
* Project context
* Troubleshooting commands
* AI explanation
* Memory search
* Project status

Automatic shell monitoring will be introduced carefully after the explicit command-execution MVP is stable.

**Status:** ⏳ Planned

---

# 🐳 PHASE 14 – Docker

**Objective:** Containerize the application.

Planned containers:

```text
┌───────────────────┐
│ React Frontend    │
└───────────────────┘

┌───────────────────┐
│ FastAPI Backend   │
└───────────────────┘

┌───────────────────┐
│ PostgreSQL        │
└───────────────────┘
```

Docker Compose will be used for local multi-container development.

**Status:** ⏳ Planned

---

# ☸️ PHASE 15 – Kubernetes

**Objective:** Deploy DevMemory AI locally using Kubernetes.

Planned components:

```text
Kubernetes
│
├── Frontend Deployment
├── Backend Deployment
├── PostgreSQL
├── Services
├── ConfigMap
├── Secrets
└── Ingress
```

Minikube will be used for local Kubernetes development.

**Status:** ⏳ Planned

---

# ☁️ PHASE 16 – AWS EKS

**Objective:** Deploy the containerized application to Amazon EKS.

Planned AWS components:

* Amazon EKS
* Amazon ECR
* IAM
* VPC
* Load Balancer
* CloudWatch
* Security Groups
* Networking

Architecture:

```text
Internet
   |
   v
AWS Load Balancer
   |
   v
EKS Cluster
   |
   ├── Frontend Pods
   ├── Backend Pods
   └── Supporting Services
```

**Status:** ⏳ Planned

---

# 🔄 PHASE 17 – GitHub Actions CI/CD

**Objective:** Automate testing, building, and deployment.

Planned pipeline:

```text
Developer
    |
    v
Git Push
    |
    v
GitHub Actions
    |
    ├── Test
    ├── Build
    ├── Docker Build
    ├── Push to ECR
    └── Deploy to EKS
```

**Status:** ⏳ Planned

---

# 🧪 PHASE 18 – Testing

Planned testing layers:

```text
Unit Tests
    ↓
API Tests
    ↓
Integration Tests
    ↓
CLI Tests
    ↓
Frontend Tests
    ↓
End-to-End Tests
```

Testing will cover:

* Backend APIs
* Database operations
* CLI functionality
* AI services
* RAG retrieval
* Frontend workflows

**Status:** ⏳ Planned

---

# 📚 PHASE 19 – Documentation & Presentation

Final documentation will include:

* System architecture
* API documentation
* Database design
* CLI documentation
* Deployment architecture
* Kubernetes architecture
* AWS architecture
* CI/CD pipeline
* AI/RAG architecture
* Project demonstration
* Interview explanation

**Status:** ⏳ Planned

---

# 🏗 Architecture Flow Diagram

```text
                         🌐 Developer
                              |
                              |
                    📁 Local Project Folder
                              |
                              v
                         💻 Terminal
                              |
                              v
                    ⚙️ DevMemory CLI
                              |
                              | HTTPS
                              v
                    ┌──────────────────┐
                    │  FastAPI Backend │
                    └────────┬─────────┘
                             |
              ┌──────────────┼──────────────┐
              |              |              |
              v              v              v
        🗄️ PostgreSQL    🤖 OpenAI       🧠 Zep
              |          Embeddings       Memory
              |              |              |
              └──────────────┼──────────────┘
                             |
                             v
                    🖥️ React Dashboard
```

---

# 🔄 Command & Troubleshooting Flow

```text
Developer
    |
    | Runs command
    v
DevMemory CLI
    |
    | Capture
    v
Command + Output + Error
    |
    v
FastAPI
    |
    v
PostgreSQL
    |
    +───────────────+
    |               |
    v               v
Error History    Project Memory
    |               |
    +───────┬───────+
            |
            v
       Embeddings
            |
            v
     Semantic Search
            |
            v
           RAG
            |
            v
        OpenAI LLM
            |
            v
    Project-Aware Answer
```

---

# 🗃️ Planned Database Entities

```text
users
projects
project_members
terminal_sessions
commands
errors
ai_analyses
solutions
solution_attempts
project_notes
tags
command_tags
error_tags
memories
feedback
audit_logs
```

---

# 🔐 Security Design

Planned security principles:

* HTTPS communication
* Environment variables for secrets
* Secure authentication
* JWT where appropriate
* Project-level access control
* API validation
* Sensitive information redaction
* Secure database credentials
* Kubernetes Secrets
* AWS IAM
* No automatic execution of dangerous AI-generated commands

The backend will not directly access the developer's local project folder.

The local CLI is responsible for collecting the required local information and communicating with the backend.

---

# 🛠 Technical Stack

### Frontend

* React
* Vite
* Axios
* React Router
* Tailwind CSS

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn
* SQLAlchemy
* Alembic

### Database

* PostgreSQL

### GenAI

* OpenAI
* Embeddings
* Semantic Search
* RAG
* Zep

### CLI

* Python
* Typer / Click
* subprocess
* pathlib
* Git integration

### DevOps

* Git
* Docker
* Docker Compose
* Kubernetes
* Minikube
* GitHub Actions

### AWS

* Amazon ECR
* Amazon EKS
* IAM
* VPC
* Load Balancer
* CloudWatch

---

# 🎯 What Makes DevMemory AI Different?

DevMemory AI is designed around **the developer's actual engineering workflow**.

Instead of simply asking:

```text
"What does this error mean?"
```

the developer can eventually ask:

```text
"Have I faced this error before?"
```

or:

```text
"How did I solve this problem in my previous project?"
```

or:

```text
"Show me the commands I used when I faced this issue."
```

The system can use:

```text
Project Context
      +
Command History
      +
Error History
      +
Solutions
      +
Engineering Notes
      +
Semantic Search
      +
AI
```

to provide project-aware assistance.

---

# 🚀 Final Goal

The final DevMemory AI architecture is intended to provide:

```text
Real Project
     +
Developer Activity
     +
Persistent Memory
     +
Semantic Retrieval
     +
AI Reasoning
     =
Project-Aware Developer Assistant
```

The ultimate goal is to create a **persistent engineering memory system** that helps developers remember, understand, and troubleshoot problems using their own previous project experience.

---

## 📊 Current Progress

```text
PHASE 0  ████████████████████ 100% ✅
PHASE 1  ████████████████░░░░  In Progress 🔄
PHASE 2  ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 3  ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 4  ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 5  ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 6  ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 7  ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 8  ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 9  ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 10 ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 11 ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 12 ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 13 ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 14 ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 15 ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 16 ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 17 ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 18 ░░░░░░░░░░░░░░░░░░░░ Planned
PHASE 19 ░░░░░░░░░░░░░░░░░░░░ Planned
```

---

## 💡 Project Objective

**Build a production-oriented GenAI + DevOps platform that remembers a developer's engineering journey and provides intelligent, project-specific troubleshooting assistance.**

**DevMemory AI — Your project's memory for every command, error, solution, and lesson.**
