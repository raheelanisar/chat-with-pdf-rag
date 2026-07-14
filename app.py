import streamlit as st
from google import genai

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# =====================================
# Gemini API
# =====================================

client = genai.Client(
    api_key="AQ.Ab8RN6JMiv6oNQcRklvjp_nS1_Kvl2IV3KFBfLHv47_IMRcO6w"
)


# =====================================
# Load PDF + Create Vector Database
# =====================================

@st.cache_resource
def load_vectorstore():

    loader = PyPDFLoader(
        "data/the-psychology-of-money-by-morgan-housel.pdf"
    )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectorstore


vectorstore = load_vectorstore()


# =====================================
# Chat Function
# =====================================

def chat_pdf(question):

    docs = vectorstore.similarity_search(
        question,
        k=2
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer the question ONLY using the given context.

If the answer is not found in the context,
reply:

"I couldn't find this information in the PDF."

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


# =====================================
# Streamlit Page
# =====================================

st.set_page_config(
    page_title="Chat with PDF using RAG",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Chat with PDF using RAG")

st.write(
    "Ask anything about **The Psychology of Money**."
)

# =====================================
# Clear Chat
# =====================================

if st.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# =====================================
# Session State
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================
# Show Previous Messages
# =====================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =====================================
# User Input
# =====================================

question = st.chat_input(
    "Ask anything about the PDF..."
)

if question:

    # Save User Question

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # Generate Answer

    with st.chat_message("assistant"):

        with st.spinner("Searching PDF..."):

            answer = chat_pdf(question)

        st.markdown(answer)

    # Save Answer

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )