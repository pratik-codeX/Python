from sentence_transformers import SentenceTransformer, util
import chromadb

# 1. Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Knowledge Base
documents = [
    "Python is used for Machine Learning",
    "Java is used for enterprise application",
    "SQL is used to manage databases",
    "HTML is used to create web pages",
    "TensorFlow is used for deep learning"
]

# 2. Generate document embeddings for ChromaDB (as a list of lists)
document_embeddings = model.encode(documents).tolist() 

# 3. Initialize ChromaDB 
client = chromadb.PersistentClient(path="./MarvellousDB")

# 4. Create collection with the correct metadata syntax for cosine distance
collection = client.get_or_create_collection(
    name="marvellous",
    metadata={"hnsw:space": "cosine"}
)

# 5. Insert documents (Fixed: passed the actual embeddings list instead of a count)
collection.upsert(
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"],
    documents=documents,
    embeddings=document_embeddings
)
print("Total Documents in DB:", collection.count())

# 6. Accept question
query = input("Enter your Question: ")

# 7. Generate PyTorch tensors for local similarity math
query_embedding = model.encode(query, convert_to_tensor=True)
doc_embedding_tensor = model.encode(documents, convert_to_tensor=True)

# 8. Calculate similarity (Fixed: extracted the 1D score vector using .squeeze())
scores = util.cos_sim(query_embedding, doc_embedding_tensor).squeeze(0)

# 9. Find top 2 matching documents
top_result = scores.topk(2)

print("\nTop 2 relevant documents:")
for index in top_result.indices:
    print(documents[index.item()])
