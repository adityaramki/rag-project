# 🏛️ MSU Broad Building RAG Chatbot

This is a Retrieval-Augmented Generation (RAG) chatbot designed to answer questions about the **Michigan State University Broad Building**.

It uses:

- LangChain to load and split PDFs into chunks  
- ChromaDB to store document chunks with vector embeddings  
- ChromaDB's built-in embedding function (`all-MiniLM-L6-v2`) to embed text
- A simple CLI interface for user queries and answers grounded in your PDFs  

---

## Features

- Load and chunk PDF content using LangChain loaders and splitters  
- Automatically embed chunks using ChromaDB’s default embedding function  
- Store embeddings and metadata persistently in a local ChromaDB vector store  
- Query the vector store with semantic search via embeddings  
- Generate grounded answers with OpenAI GPT (optional, requires API key)

---

## Project Structure
<pre>
msu-broad-rag/
├── README.md
├── chroma_db
├── data
│   └── Broad Tour.pdf
├── fill_db.py
├── query.py
└── requirements.txt

</pre>

---

## Setup/Usage Instructions
### 1. Clone and install dependencies

```bash
git clone https://github.com/yourusername/msu-broad-chatbot.git
cd msu-broad-chatbot
pip install -r requirements.txt
```

### 2. Add your PDFs
Place all the PDFs inside data/. This RAG model can be used for any topic but there is already a sample pdf about the Broad Building inside data/ to start.

### 3. Provide an OpenAI API key
To generate natural language answers based on retrieved documents, this project uses OpenAI’s GPT models. You need to provide your OpenAI API key in a .env file like this:
```bash
OPENAI_API_KEY=your-api-key-here
```

### 4. Run fill_db.py
This will make the vector chroma database and you have to do this before you can prompt any queries.

---
## Troubleshooting
- If you don’t get relevant answers, make sure the PDFs are properly loaded and indexed.

- Check that the collection is created with embedding_function=DefaultEmbeddingFunction() to enable embeddings.

- To clear and rebuild your database, delete the chroma_db/ folder and rerun the loader.

