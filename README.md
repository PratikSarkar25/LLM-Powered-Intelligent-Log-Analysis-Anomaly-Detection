# LLM-Powered Intelligent Log Analysis & Anomaly Detection

## Overview

LLM-Powered Intelligent Log Analysis & Anomaly Detection is a hybrid AI-driven observability system designed to automate log understanding, anomaly detection, and root cause analysis using Large Language Models (LLMs), semantic embeddings, clustering algorithms, and Retrieval-Augmented Generation (RAG).

The project combines traditional log parsing techniques with modern AI reasoning to provide intelligent insights from raw system logs.

---

# Features

* Intelligent log analysis using LLMs
* Hybrid anomaly detection pipeline
* Semantic log clustering
* Retrieval-Augmented Generation (RAG)
* Natural language querying over logs
* Automated issue summarization
* Root cause analysis assistance
* Real-time scalable pipeline support

---

# Project Architecture

```text
Raw Log File Uploaded
        ↓
User Query
        ↓
LLM Intent Router
 ┌────────────────────┐
 │ Query Type Detect  │
 └────────────────────┘
   ↓            ↓
Direct QA    Cluster Path
(raw logs)   (Drain + embeddings)
   ↓            ↓
Answer       Match Cluster
                ↓
          Retrieve Context
                ↓
             LLM Reasoning
                ↓
         Intelligent Response
```

---

# Tech Stack

## Core Technologies

* Python
* Large Language Models (LLMs)
* Sentence Transformers
* FAISS Vector Database
* Drain Log Parser
* Pandas
* Scikit-learn
* NumPy

## Optional Frontend/API

* Streamlit
* FastAPI

---

# Folder Structure

```text
project/
│
├── data/
│   └── logs.txt
│
├── parser.py
├── rag_engine.py
├── anomaly.py
├── main.py
├── requirements.txt
├── README.md
│
└── models/
```

---

# Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Upgrade pip

```bash
pip install --upgrade pip
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Sample requirements.txt

```text
pandas
numpy
scikit-learn
sentence-transformers
faiss-cpu
transformers
torch
openai
streamlit
fastapi
uvicorn
```

---

# Running the Project

## Run Main Pipeline

```bash
python main.py
```

---

# Example Workflow

```python
from parser import load_logs
from rag_engine import build_index
from anomaly import detect_anomalies


def main():

    print('Loading logs...')
    df = load_logs()

    print(f'Total logs loaded: {len(df)}')

    print('Running anomaly detection...')
    anomalies = detect_anomalies(df)

    print('\nDetected Issues:')
    for issue in anomalies:
        print(f' - {issue}')


if __name__ == '__main__':
    main()
```

---

# Running Streamlit Dashboard (Optional)

```bash
streamlit run app.py
```

---

# Running FastAPI Server (Optional)

```bash
uvicorn api:app --reload
```

---

# Input Log Format

```text
2026-05-20 10:22:15 ERROR Database connection failed
2026-05-20 10:22:18 INFO Retrying database connection
2026-05-20 10:22:22 WARNING High memory usage detected
```

---

# Core Modules

## parser.py

Handles log loading and preprocessing.

## rag_engine.py

Builds semantic embedding index and retrieval pipeline.

## anomaly.py

Performs anomaly detection using hybrid techniques.

## main.py

Controls the complete workflow execution.

---

# Future Improvements

* Multi-agent log reasoning
* Real-time streaming support
* Kubernetes log integration
* Grafana/Splunk integration
* Autonomous remediation suggestions
* Predictive failure detection

---

# Applications

* DevOps Monitoring
* Cloud Infrastructure Observability
* Security Log Analysis
* AI-Assisted Incident Response
* Distributed System Debugging
* Site Reliability Engineering (SRE)

---

# Research Inspiration

This project is inspired by modern research in:

* Drain
* DeepLog
* HELP
* LogRules
* MicroRCA-Agent
* LogSage

---

# Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# License

This project is licensed under the MIT License.

---

# Author

Pratik Sarkar
MSc Data Science & Artificial Intelligence
Ramakrishna Mission Vivekananda Educational and Research Institute
