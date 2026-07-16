# 🚀 RAG Pipeline using Langflow + Ollama + ChromaDB + Groq

An end-to-end **Retrieval-Augmented Generation (RAG)** pipeline built using **Langflow**, **Ollama Embeddings**, **ChromaDB**, and **Groq Llama 3.1**. This project demonstrates how to create a semantic search system that retrieves relevant information from a document before generating accurate AI responses.

---

## 📌 Project Overview

This project ingests a document containing **1000+ E-commerce Test Cases**, converts the content into vector embeddings, stores them in a ChromaDB vector database, and answers user questions using Retrieval-Augmented Generation (RAG).

Instead of sending the entire document to the LLM, the pipeline retrieves only the most relevant chunks, resulting in faster, more accurate, and context-aware responses.

---

## 🏗 Architecture

```
Read File
    │
    ▼
Split Text into Chunks
    │
    ▼
Generate Embeddings (Ollama)
    │
    ▼
Store Embeddings in ChromaDB
    │
    ▼
User Question
    │
    ▼
Semantic Search
    │
    ▼
Retrieve Relevant Chunks
    │
    ▼
Prompt Template
    │
    ▼
Groq Llama 3.1
    │
    ▼
Generated Answer
```

---

## 🛠 Tech Stack

- **Langflow**
- **Ollama**
- **Nomic Embed Text**
- **ChromaDB**
- **Groq**
- **Llama 3.1 8B Instant**

---

## 📂 Dataset

The project uses a document containing **1000+ E-commerce Test Cases**, including:

- Login
- Registration
- Dashboard
- Shopping Cart
- Product Search
- Checkout
- Orders
- User Profile

---

## ⚙ Configuration

### Chunk Size

- Chunk Size: **1000**
- Chunk Overlap: **200**

### Embedding Model

```
nomic-embed-text:latest
```

### Vector Database

```
ChromaDB
```

### LLM

```
Groq
Model: llama-3.1-8b-instant
```

---

## 🔄 Workflow

1. Read the uploaded document.
2. Split the document into smaller chunks.
3. Generate embeddings using Ollama.
4. Store embeddings in ChromaDB.
5. Accept a user question.
6. Retrieve the most relevant chunks.
7. Build a prompt using the retrieved context.
8. Generate an accurate answer using Groq.

---

## 📷 Pipeline Screenshot

> Add your Langflow pipeline screenshot here.

Example:

```
images/rag_pipeline.png
```

---

## 🎯 Key Features

- Low-code AI workflow using Langflow
- Local embedding generation with Ollama
- Semantic Search using ChromaDB
- Context-aware responses using RAG
- Groq-powered LLM inference
- Easily extendable for any PDF or document

---

## 📚 Learning Outcomes

This project helped me understand:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embeddings
- Semantic Search
- Prompt Engineering
- Langflow Workflows
- Local AI with Ollama
- ChromaDB Integration

---

## 🚀 Future Enhancements

- Build the same pipeline using **n8n**
- Support PDF uploads
- Add conversational memory
- Multi-document retrieval
- Hybrid Search
- Metadata filtering
- Streaming responses

---

## 👩‍💻 Author

**Rekha Govardhan**

**Senior QA Engineer | AI & GenAI Enthusiast**

- 11+ Years in Software Testing
- Banking & Financial Services Domain
- Manual Testing | API Testing | AI Testing
- Learning RAG, AI Agents, Langflow, n8n & LLM Applications

---

## ⭐ If you found this project useful, don't forget to Star the repository!