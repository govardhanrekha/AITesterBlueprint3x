# 📚 Local RAG Chat

A beginner-friendly **Retrieval Augmented Generation (RAG)** app that lets you
upload a PDF and ask questions about it — answered by a **local** LLM through
**Ollama**. No API keys, no paid services, everything runs on your machine.

---

## How it works

```
PDF upload
   │
   ▼
PyPDFLoader            (ingest.py)  → splits PDF into pages
   │
   ▼
RecursiveCharacterTextSplitter       → splits pages into 1000-char chunks (200 overlap)
   │
   ▼
HuggingFace all-MiniLM-L6-v2         → turns each chunk into an embedding vector
   │
   ▼
ChromaDB                             → stores the vectors locally (chroma_db/)
   │
   ▼
User question ──► retrieve top-4 chunks    (rag.py)
   │
   ▼
Ollama (llama3.2 / mistral / neural-chat)  → answers using only the retrieved chunks
```

## Project structure

```
Project_06_RAG/
├── app.py             # Streamlit UI
├── ingest.py          # PDF loading, chunking, embeddings, ChromaDB storage
├── rag.py             # Retrieval + answer generation with Ollama
├── config.py          # All settings (chunk size, model names, paths...)
├── requirements.txt   # Python dependencies
├── README.md          # This file
├── uploads/           # Uploaded PDFs (auto-created)
└── chroma_db/         # ChromaDB vector store (auto-created)
```

---

## 1. Prerequisites

- **Python 3.9+**
- **Ollama** installed and running locally → https://ollama.com/download

Verify Ollama is installed:

```bash
ollama --version
```

## 2. Pull a local model

Choose one or more of the supported models:

```bash
ollama pull llama3.2
# or
ollama pull mistral
# or
ollama pull neural-chat
```

Make sure the Ollama background service is running:

```bash
ollama serve
```

(On macOS/Windows the Ollama desktop app usually keeps this running for you.)

## 3. Set up the Python environment

From inside the project folder:

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

> The first run will also download the `all-MiniLM-L6-v2` embedding model
> (~90MB) from HuggingFace automatically — this only happens once.

## 4. Configuration

Edit `config.py` to customize:

- **OLLAMA_MODEL**: Change the default model (llama3.2, mistral, neural-chat)
- **CHROMA_DIR**: Path where vector embeddings are stored
- **UPLOAD_DIR**: Path where uploaded PDFs are saved
- **COLLECTION_NAME**: ChromaDB collection name

## 5. Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## Troubleshooting

### Ollama connection errors
- Ensure Ollama service is running: `ollama serve`
- Check if Ollama is accessible at `http://localhost:11434`

### Model not found errors
- Pull the model first: `ollama pull <model_name>`
- Verify it's available: `ollama list`

### Embedding/ChromaDB errors
- Delete the `chroma_db/` folder to reset the vector store
- Reinstall chromadb: `pip install --upgrade chromadb`

### Memory issues
- Try a smaller model: `ollama pull neural-chat` (smaller than llama3.2)
- Reduce chunk overlap in `config.py` if needed

---

## Features

✅ Dark theme UI  
✅ PDF upload & chunking  
✅ Local embeddings (HuggingFace)  
✅ Vector search (ChromaDB)  
✅ Local LLM answers (Ollama)  
✅ Chat history  
✅ No external APIs  
✅ Fully offline support  

---

## License

MIT

Streamlit will print a local URL (usually `http://localhost:8501`) and should
open it in your default browser automatically.

If the browser doesn't open by itself, just copy that URL into your browser
manually. If port `8501` is already in use, run:

```bash
streamlit run app.py --server.port 8502
```

## 5. Using the app

1. In the sidebar, choose which local model to use (`llama3.2` or `mistral`).
2. Upload a PDF file.
3. Wait for indexing to finish — you'll see **Pages**, **Chunks**,
   **Embedding Dim**, and **Stored Vectors** displayed at the top.
4. Type a question in the box and click **Ask**.
5. Expand **🔎 Retrieved chunks** to see exactly which passages were used,
   then read the generated **Answer** below it.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `Could not reach the Ollama model` error | Run `ollama serve` in a terminal and make sure you've pulled the model with `ollama pull llama3.2` |
| Streamlit doesn't open a browser tab | Manually open the URL printed in the terminal (e.g. `http://localhost:8501`) |
| Port already in use | `streamlit run app.py --server.port 8502` |
| Slow first upload | The embedding model downloads once and is cached afterwards — later uploads are faster |
| Re-uploading a PDF | The app clears the previous vector store automatically so old and new documents don't mix |

---

## Notes

- Everything here — the embedding model, the vector database, and the LLM —
  runs **entirely on your own machine**. No external API calls, no API keys.
- Uploaded PDFs are saved to `uploaded_pdfs/` and vectors to `chroma_db/`
  inside the project folder; delete these folders anytime to reset the app.
