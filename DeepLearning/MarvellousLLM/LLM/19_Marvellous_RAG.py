from sentence_transformers import SentenceTransformer, util
import chromadb
from ollama import chat

# 1. Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to Existing Chromadb
client = chromadb.PersistentClient(path="./MarvellousDB")

collection = client.get_collection(name="marvellous")

# give the question
query = input("Enter your Question: ")

# generate query embedding
query_embedding = model.encode(query, convert_to_tensor=True)

# retrive top 2 result
results = collection.query(query_embeddings = [query_embedding.tolist()],n_results=2)

# Create context from retrived documents
documents = results["documents"][0]

context = "\n".join(documents)

print("Retrived context :")
print(context)

#create prompt for LLM

prompt = f"""
            
            Answer the question using only the given context.
            
            Context : {context}
            Question : {query}
            
            If the answer is not available in context,
            Say "Information not Available"
            
         """

# Send the context and Question to ollama (llama)
response= chat(
    model = "llama3.2:1b",
    messages =[
        {
            "role" : "user",
            "content" : prompt    
        }
    ]
)

answer = response.message.content

print("Marvellous GENAI : RAG answer : ")
print(answer)