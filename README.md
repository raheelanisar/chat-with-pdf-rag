# chat-with-pdf-rag
# 📚 Chat with PDF using RAG

An AI-powered PDF Question Answering system built using Retrieval-Augmented Generation (RAG). Users can upload or use a PDF document and ask natural language questions. The system retrieves the most relevant information from the document using FAISS and HuggingFace embeddings before generating accurate answers with Google's Gemini model.

---

## 🚀 Features

- Load PDF documents
- Split PDF into text chunks
- Generate embeddings using HuggingFace
- Store embeddings in FAISS Vector Database
- Retrieve relevant context using similarity search
- Answer questions using Google Gemini
- User-friendly Gradio Interface

---

## 🛠️ Technologies Used

- Python
- LangChain
- HuggingFace Embeddings
- FAISS
- Google Gemini API
- Gradio
- PyPDFLoader

---

## 📂 Project Structure

```
chat-with-pdf-rag/
│
├── data/
│   └── the-psychology-of-money-by-morgan-housel.pdf
│
├── Chat_with_PDF_RAG.ipynb
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/chat-with-pdf-rag.git
```

Move into the project

```bash
cd chat-with-pdf-rag
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:7860
```

---

## 📖 Example Questions

- What is the psychology of money?
- What does the author say about saving?
- What is the role of luck in wealth?
- How does the author define wealth?
- Why is psychology more important than mathematics in finance?
<img width="640" height="313" alt="image" src="https://github.com/user-attachments/assets/1bbda77c-b3c0-424a-9d82-d5509650d04a" />


---

## 📸 Demo

<img width="640" height="320" alt="image" src="https://github.com/user-attachments/assets/b9b1da07-eb56-4c2f-9403-89fdb42dde06" />
<img width="640" height="316" alt="image" src="https://github.com/user-attachments/assets/0d9ef411-7bee-4f80-9098-3e441bcc1a37" />
<img width="640" height="317" alt="image" src="https://github.com/user-attachments/assets/bc979f7a-e20d-4071-83c6-ea9df59fdc41" />
<img width="640" height="317" alt="image" src="https://github.com/user-attachments/assets/af09ac04-fff9-41de-b2cb-f47505e50f03" />
<img width="640" height="315" alt="image" src="https://github.com/user-attachments/assets/b896d702-f6a9-4069-94cb-0c643d6694b7" />



---




app.py screenshots

<img width="640" height="314" alt="image" src="https://github.com/user-attachments/assets/074e05c2-0e78-4bde-8de5-b263ece0d135" />
<img width="639" height="319" alt="image" src="https://github.com/user-attachments/assets/b6a4ba68-395c-4dab-b2db-5c9c8ff310c8" />


---

## 👩‍💻 Author

Raheela Nisar 

BS Computer Science

Fatima Jinnah Women University

---

## 📜 License

This project is developed for educational purposes.
