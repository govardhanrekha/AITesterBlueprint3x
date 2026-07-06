"""
Streamlit front-end for the local RAG application.

Flow:
1. User uploads a PDF.
2. We run the ingestion pipeline (ingest.py) and show stats.
3. User asks a question.
4. We retrieve the top matching chunks and show them.
5. We ask the local Ollama model to answer using those chunks (rag.py).
"""

import os
import time

import streamlit as st

import config
from ingest import ingest_pdf
from rag import answer_question

# ---------------------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Local RAG Chat",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Dark theme styling
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Overall app background */
    .stApp {
        background-color: #0e1117;
        color: #e6e6e6;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #131720;
        border-right: 1px solid #262b36;
    }

    /* Headings */
    h1, h2, h3, h4 {
        color: #f5f5f5 !important;
    }

    /* Metric / stat cards */
    .stat-card {
        background-color: #1a1f2b;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        padding: 18px 16px;
        text-align: center;
    }
    .stat-value {
        font-size: 28px;
        font-weight: 700;
        color: #7dd3fc;
    }
    .stat-label {
        font-size: 13px;
        color: #9aa4b2;
        margin-top: 4px;
    }

    /* Chunk cards */
    .chunk-card {
        background-color: #151a24;
        border-left: 3px solid #7dd3fc;
        border-radius: 8px;
        padding: 12px 14px;
        margin-bottom: 10px;
        font-size: 14px;
        color: #d1d5db;
    }
    .chunk-title {
        font-size: 12px;
        color: #7dd3fc;
        font-weight: 600;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }

    /* Answer box */
    .answer-box {
        background-color: #12201c;
        border: 1px solid #1f6f4a;
        border-radius: 12px;
        padding: 18px;
        color: #eafff3;
        font-size: 15.5px;
        line-height: 1.55;
    }

    /* Buttons */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }

    /* Text input */
    .stTextInput>div>div>input {
        background-color: #1a1f2b;
        color: #e6e6e6;
        border-radius: 8px;
        border: 1px solid #2a2f3d;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "stats" not in st.session_state:
    st.session_state.stats = None
if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None
if "history" not in st.session_state:
    st.session_state.history = []  # list of {question, answer, chunks}

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## ⚙️ Setup")

    model_name = st.radio(
        "Local Ollama model",
        options=config.AVAILABLE_MODELS,
        index=config.AVAILABLE_MODELS.index(config.DEFAULT_MODEL),
        help="Make sure this model has been pulled with `ollama pull <model>`.",
    )

    st.markdown("---")
    st.markdown("### 📄 Upload a PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        is_new_file = uploaded_file.name != st.session_state.pdf_name
        if is_new_file:
            save_path = os.path.join(config.UPLOAD_DIR, uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            with st.spinner("Reading PDF, splitting text, and building embeddings..."):
                start = time.time()
                vectorstore, stats = ingest_pdf(save_path)
                elapsed = time.time() - start

            st.session_state.vectorstore = vectorstore
            st.session_state.stats = stats
            st.session_state.pdf_name = uploaded_file.name
            st.session_state.history = []
            st.success(f"Indexed in {elapsed:.1f}s ✅")

    st.markdown("---")
    st.caption(
        "This app runs 100% locally: HuggingFace embeddings, ChromaDB, "
        "and an Ollama model. No API keys, no paid services."
    )

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown("# 📚 Local RAG Chat")
st.markdown(
    "Ask questions about your PDF. Answers are generated locally with "
    "**Ollama**, grounded in text retrieved from **ChromaDB**."
)

if st.session_state.pdf_name:
    st.markdown(f"**Current document:** `{st.session_state.pdf_name}`")

st.markdown("")

# ---------------------------------------------------------------------------
# Stats row
# ---------------------------------------------------------------------------
if st.session_state.stats:
    stats = st.session_state.stats
    cols = st.columns(4)
    labels_values = [
        ("Pages", stats["num_pages"]),
        ("Chunks", stats["num_chunks"]),
        ("Embedding Dim", stats["embedding_dim"]),
        ("Stored Vectors", stats["num_vectors"]),
    ]
    for col, (label, value) in zip(cols, labels_values):
        with col:
            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-value">{value}</div>
                    <div class="stat-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown("")
else:
    st.info("Upload a PDF from the sidebar to get started.")

# ---------------------------------------------------------------------------
# Question input
# ---------------------------------------------------------------------------
st.markdown("### 💬 Ask a question")

with st.form(key="question_form", clear_on_submit=True):
    query = st.text_input(
        "Your question",
        placeholder="e.g. What is the main conclusion of this document?",
        label_visibility="collapsed",
    )
    submitted = st.form_submit_button("Ask")

if submitted and query:
    if st.session_state.vectorstore is None:
        st.warning("Please upload a PDF first.")
    else:
        with st.spinner(f"Retrieving context and asking {model_name}..."):
            try:
                answer, docs = answer_question(
                    st.session_state.vectorstore,
                    query,
                    k=config.TOP_K,
                    model_name=model_name,
                )
                st.session_state.history.insert(
                    0, {"question": query, "answer": answer, "chunks": docs}
                )
            except Exception as e:
                st.error(
                    f"Could not reach the Ollama model '{model_name}'. "
                    f"Make sure Ollama is running (`ollama serve`) and the "
                    f"model is pulled (`ollama pull {model_name}`).\n\n"
                    f"Details: {e}"
                )

# ---------------------------------------------------------------------------
# Conversation history
# ---------------------------------------------------------------------------
for turn in st.session_state.history:
    st.markdown("---")
    st.markdown(f"**Q: {turn['question']}**")

    with st.expander(f"🔎 Retrieved chunks ({len(turn['chunks'])})", expanded=False):
        for i, doc in enumerate(turn["chunks"], start=1):
            page = doc.metadata.get("page", "?")
            st.markdown(
                f"""
                <div class="chunk-card">
                    <div class="chunk-title">Chunk {i} · Page {page}</div>
                    {doc.page_content}
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        f"""
        <div class="answer-box">
            <strong>Answer</strong><br><br>{turn['answer']}
        </div>
        """,
        unsafe_allow_html=True,
    )
