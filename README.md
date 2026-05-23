# Enterprise AI Assistant

## Overview
Enterprise AI Assistant is an AI-powered document question-answering system developed using Retrieval-Augmented Generation (RAG). The application allows users to upload documents, process their content, store embeddings in a vector database, and ask questions in natural language.

The system retrieves relevant information from uploaded documents and generates accurate responses using a Large Language Model (LLM).

---

## Features

- Document upload and processing
- Text extraction from PDF documents
- Text chunking using LangChain
- Embedding generation
- Vector database integration using Pinecone
- Retrieval-Augmented Generation (RAG) pipeline
- Natural language question answering
- FastAPI backend API
- Scalable architecture for enterprise use

---

## Technologies Used

### Programming Language
- Python

### Backend Framework
- FastAPI

### AI and Machine Learning
- LangChain
- Large Language Model (LLM)

### Vector Database
- Pinecone

### Data Processing
- PDF text extraction
- Recursive text splitting

### Development Environment
- VS Code
- Git
- GitHub

---

## Project Structure

```text
Enterprise_AI_Assistant/
│
├── backend/
│   ├── embeddings.py
│   ├── llm.py
│   ├── main.py
│   ├── memory.py
│   ├── pdf_handler.py
│   ├── pinecone_db.py
│   ├── rag.py
│   └── splitter.py
│
├── frontend/
│   └── app.py
│
├── documents/
│
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Working Procedure

### Step 1: Document Upload
Users upload PDF documents into the system.

### Step 2: Text Extraction
The system extracts text from uploaded PDF files.

### Step 3: Text Splitting
Large text is divided into smaller chunks using RecursiveCharacterTextSplitter.

### Step 4: Embedding Generation
Embeddings are generated from text chunks.

### Step 5: Store Embeddings
Generated embeddings are stored in Pinecone vector database.

### Step 6: User Query
Users ask questions through the interface.

### Step 7: Context Retrieval
The system retrieves the most relevant document chunks.

### Step 8: Response Generation
The LLM generates a contextual answer using retrieved information.

---

## RAG Workflow

User Query
↓
Retrieve Relevant Context
↓
Vector Database (Pinecone)
↓
Large Language Model
↓
Generate Response

---

## Installation Steps

### Clone Repository

```bash
git clone https://github.com/Rafiyagafoor/Enterprise_AI_Assistant.git
```

### Navigate to Project

```bash
cd Enterprise_AI_Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn backend.main:app --reload
```

---

## Run Frontend

```bash
streamlit run frontend/app.py
```

---

## Future Enhancements

- Multiple document support
- Voice interaction
- Chat history
- User authentication
- Multi-language support
- Cloud deployment
- Advanced memory system

---

## Applications

- Enterprise knowledge assistants
- Customer support systems
- Document search systems
- Educational assistants
- Internal company chatbot systems

---

## Author

Rafiya Gafoor

BTech Computer Science Graduate  
Data Science Learner
