from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

from chromadb.utils import embedding_functions

default_ef = embedding_functions.DefaultEmbeddingFunction()

DATA_PATH = r"data" 
CHROMA_PATH = r"chroma_db"

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(name="my_collection", embedding_function=default_ef)

loader = PyPDFDirectoryLoader(DATA_PATH)

raw_documents = loader.load() # all the documents in data folder in one place

text_splitter = RecursiveCharacterTextSplitter ( 
    chunk_size = 300,
    chunk_overlap = 100,
    length_function = len,
    is_separator_regex=False
)

chunks = text_splitter.split_documents(raw_documents) # splits documents into various chunks

documents = []
metadata = []
ids = []

i = 0

for chunk in chunks: 
    documents.append(chunk.page_content) 
    ids.append("ID" + str(i))
    metadata.append(chunk.metadata)

    i+=1

collection.upsert( # feed all data into chroma db
    documents=documents,
    metadatas=metadata,
    ids=ids
)
    


