import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import chromadb
from openai import OpenAI
from dotenv import load_dotenv

from chromadb.utils import embedding_functions

default_ef = embedding_functions.DefaultEmbeddingFunction()

load_dotenv()

# setting the environment

DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(name="my_collection", embedding_function= default_ef)


user_query = input("What do you want to know about the Broad Building at MSU?\n\n") 

results = collection.query( # find 3 relevant vector embeddings when compared to user query embedding
    query_texts=[user_query],
    n_results=3,
    include=['documents', 'embeddings', 'metadatas']
)

#print(results['embeddings'])
print(results['documents'])
#print(results['metadatas'])
'''
client = OpenAI()

system_prompt = """
You are a helpful AI assistant. You answer questions about Michigan State University's Broad Building. 
But you only answer based on knowledge I'm providing you. You don't use your internal 
knowledge and you don't make things up.
If you don't know the answer, just say: I don't know
--------------------
The data:
"""+str(results['documents'])+"""
"""

#print(system_prompt)

response = client.chat.completions.create(
    model="gpt-4o",
    messages = [
        {"role":"system","content":system_prompt},
        {"role":"user","content":user_query}    
    ]
)

print("\n\n---------------------\n\n")

print(response.choices[0].message.content)

'''
