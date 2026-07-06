"""
rag.py
Compatible with app.py + ingest.py
"""

from ollama import Client

client = Client(host="http://localhost:11434")


def answer_question(vectorstore, question, k=4, model_name="gemma3:1b"):
    """
    Retrieve relevant chunks from Chroma and ask Ollama.
    """

    docs = vectorstore.similarity_search(question, k=k)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the provided context.

If the answer is not contained in the context, reply:
"I don't know based on the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        response = client.generate(
            model=model_name,
            prompt=prompt,
        )

        answer = response["response"]

        return answer, docs

    except Exception as e:
        return f"Ollama Error: {e}", docs