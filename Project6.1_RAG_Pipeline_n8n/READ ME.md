# 📚 AI RAG Chatbot using n8n + Supabase + Gemini

> A beginner-friendly Retrieval-Augmented Generation (RAG) application built using **n8n**, **Google Gemini**, and **Supabase (pgvector)**. The chatbot ingests PDF/TXT documents, generates vector embeddings, stores them in a vector database, and answers user questions using Retrieval-Augmented Generation.

---

## 🚀 Project Overview

This project demonstrates how to build a complete RAG pipeline without writing backend code.

The application can:

- 📄 Upload PDF/TXT documents
- 📖 Extract document content
- ✂️ Split documents into chunks
- 🧠 Generate embeddings using Gemini
- 🗄️ Store embeddings in Supabase (pgvector)
- 💬 Accept natural language questions
- 🔍 Retrieve the most relevant document chunks
- 🤖 Generate accurate answers using Gemini
- 🚫 Avoid hallucinations by answering only from uploaded documents

---

# 🏗️ Architecture

![Architecture](architecture.png)

---

# 🛠️ Tech Stack

| Component | Technology |
|------------|------------|
| Workflow Automation | n8n |
| LLM | Google Gemini |
| Embedding Model | Google Gemini Embeddings |
| Vector Database | Supabase (pgvector) |
| Document Loader | n8n Default Data Loader |
| Text Splitter | Recursive Character Text Splitter |
| AI Agent | n8n AI Agent |

---

# 📂 Project Structure

```
basic-rag-n8n/
│
├── README.md
├── architecture.png
├── workflow.json
│
├── screenshots/
│   ├── workflow.png
│   ├── ingestion.png
│   ├── retrieval.png
│   ├── output.png
│
├── sample-data/
│   └── PRD.pdf
│
└── docs/
    └── setup-guide.md
```

---

# 🔄 RAG Workflow

## Phase 1 – Document Ingestion

```
Upload PDF
      │
      ▼
Default Data Loader
      │
      ▼
Recursive Character Text Splitter
      │
      ▼
Gemini Embeddings
      │
      ▼
Supabase Vector Store
```

---

## Phase 2 – Retrieval

```
User Question
      │
      ▼
AI Agent
      │
      ▼
Generate Query Embedding
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Top-K Chunks
      │
      ▼
Gemini
      │
      ▼
Final Answer
```

---

# 📸 Workflow Screenshot

> Replace with your workflow screenshot.

![Workflow](screenshots/workflow.png)

---

# 📸 Document Ingestion Pipeline

The ingestion pipeline performs:

- Upload document
- Read document
- Split into chunks
- Generate embeddings
- Store vectors in Supabase

![Ingestion](screenshots/ingestion.png)

---

# 📸 Retrieval Pipeline

The retrieval pipeline:

- Accepts user questions
- Generates query embeddings
- Searches similar vectors
- Retrieves relevant context
- Generates the final response

![Retrieval](screenshots/retrieval.png)

---

# 📸 Chat Output

Example question:

```
Who is the target audience?
```

Example response:

```
Primary Users

• Product Managers
• UX Designers
• Marketing Teams

Secondary Users

• Engineering Teams
• Business Executives
```

![Output](screenshots/output.png)

---

# ⚙️ How It Works

## Step 1

Upload a PDF or TXT document.

↓

## Step 2

The document is converted into plain text.

↓

## Step 3

The text is split into smaller chunks.

↓

## Step 4

Each chunk is converted into an embedding vector.

↓

## Step 5

Embeddings are stored in Supabase.

↓

## Step 6

The user asks a question.

↓

## Step 7

The question is converted into an embedding.

↓

## Step 8

The vector database retrieves the Top-K most relevant chunks.

↓

## Step 9

The retrieved context is passed to Gemini.

↓

## Step 10

Gemini generates an answer grounded in the uploaded document.

---

# 🧠 Prompt Used

The AI Agent is instructed to answer only from retrieved document context. The prompt is based on the uploaded document and includes the instruction:

> "Use the retrieved document to answer questions. If the information cannot be found, respond with 'I cannot find the information'." :contentReference[oaicite:0]{index=0}

---

# ✨ Features

- PDF Upload
- TXT Upload
- AI Agent
- Semantic Search
- Vector Embeddings
- Context Retrieval
- Top-K Retrieval
- Supabase Vector Database
- Gemini Integration
- Low-Code Workflow
- Beginner Friendly
- Modular Design

---

# 📈 Future Enhancements

- Multi-document support
- Metadata filtering
- Conversation memory
- Hybrid search (Keyword + Vector)
- Reranking
- Source citations
- Streaming responses
- OCR for scanned PDFs
- Role-based access
- Docker deployment

---

# 🧪 Sample Questions

```
Who is the target audience?

Summarize the PRD.

What are the functional requirements?

List the acceptance criteria.

Who are the stakeholders?

What assumptions are mentioned?

What is the project scope?
```

---

# 📊 Key Learnings

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Vector embeddings
- Semantic search
- Chunking strategy
- Context retrieval
- Prompt engineering
- AI workflow orchestration using n8n
- Integration with Supabase pgvector
- Gemini LLM integration

---

# 🙌 Acknowledgements

- n8n
- Google Gemini
- Supabase
- pgvector

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.