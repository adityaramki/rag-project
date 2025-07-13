# 🏛️ MSU Broad Building RAG Chatbot

This is a Retrieval-Augmented Generation (RAG) chatbot designed to answer questions about the **Michigan State University Broad Building**.

It uses:

- **LangChain** to load and split PDFs into chunks  
- **ChromaDB** to store document chunks with vector embeddings  
- ChromaDB's built-in embedding function (`all-MiniLM-L6-v2`) to embed text
- A simple CLI interface for user queries and answers grounded in your PDFs  

---

## Features

- Load and chunk PDF content using LangChain loaders and splitters  
- Automatically embed chunks using ChromaDB’s default embedding function  
- Store embeddings and metadata persistently in a local ChromaDB vector store  
- Query the vector store with semantic search via embeddings  
- Generate grounded answers with OpenAI GPT (optional, requires API key)  





