import gradio as gr
from google import genai

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# -----------------------------
# Gemini API
# -----------------------------

client = genai.Client(
    api_key="AQ.Ab8RN6IXSGhG3ZFyTOclxHZLfFq4CjQExBYRpJbnqqcK2NPF3A"
)

# -----------------------------
# Load PDF
# -----------------------------

loader = PyPDFLoader("data/the-psychology-of-money-by-morgan-housel.pdf")
documents = loader.load()

# -----------------------------
# Split Documents
# -----------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

# -----------------------------
# Embeddings
# -----------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# FAISS Vector Store
# -----------------------------

vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embedding_model
)

# -----------------------------
# Chat Function
# -----------------------------

def chat_pdf(question):

    docs = vectorstore.similarity_search(question, k=2)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question only from the given context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text


# -----------------------------
# Gradio UI
# -----------------------------

demo = gr.Interface(
    fn=chat_pdf,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask a Question"
    ),
    outputs=gr.Textbox(label="Answer"),
    title="Chat with PDF using RAG",
    description="Ask anything about The Psychology of Money PDF."
)

demo.launch()