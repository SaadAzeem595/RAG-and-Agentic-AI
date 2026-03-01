# 📄 DocChat – Multi-Agent RAG System

A production-style Multi-Agent Retrieval-Augmented Generation (RAG) system designed to extract accurate, source-grounded answers from long and structured documents such as PDFs, research papers, and technical reports.

Unlike traditional single-LLM chatbots, DocChat uses a multi-agent architecture with verification to reduce hallucinations and improve factual reliability.

---

## 🚀 Features

- 📂 Upload long documents (PDF, reports, structured files)
- 🔎 Hybrid Retrieval (BM25 + Vector Search)
- 🤖 Multi-Agent Architecture
- ✅ Hallucination Detection & Verification
- 🔁 Self-Correction Mechanism
- 🧠 Context-aware reasoning
- 🎛️ Interactive Gradio UI
- 📊 Handles complex structured documents with tables and dense content

---

## 🏗️ Architecture Overview

DocChat follows a multi-step, verification-driven pipeline:

### 1️⃣ Hybrid Retriever
- Combines:
  - BM25 keyword search
  - Vector embeddings (semantic search)
- Retrieves the most relevant document chunks

### 2️⃣ Research Agent
- Analyzes retrieved content
- Generates structured answer

### 3️⃣ Verification Agent
- Cross-checks generated response
- Detects unsupported claims
- Flags hallucinations

### 4️⃣ Self-Correction Layer
- If contradiction found:
  - Re-runs research step
  - Produces improved grounded response

This ensures high factual reliability.

---

## 🧠 Why Not Use a Single LLM?

Traditional chatbots:
- Struggle with long documents
- Misinterpret tables
- Fabricate citations
- Ignore footnotes
- Hallucinate when uncertain

DocChat solves this with:
- Hybrid retrieval
- Multi-agent reasoning
- Verification pipeline
- Controlled generation

---

## 🛠️ Tech Stack

- Python
- LangChain
- ChromaDB (Vector Database)
- BM25 Retriever
- IBM Watsonx / LLM APIs
- Gradio (UI)
- Embedding Models

---

## 📂 Project Structure
DocChat-Multi-Agent-RAG/
│
├── app.py
├── retriever.py
├── research_agent.py
├── verification_agent.py
├── utils/
├── document_cache/
├── requirements.txt
