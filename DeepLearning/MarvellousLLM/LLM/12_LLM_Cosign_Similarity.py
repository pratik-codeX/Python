from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences1 = "Python is a programming language"
sentences2 = "Python is used for software development"

embeddings1 = model.encode(sentences1,convert_to_tensor = True)
embeddings2 = model.encode(sentences2,convert_to_tensor = True)

# calculate cosine similarity
similarity = util.cos_sim(embeddings1,embeddings2)

print("Sentence 1 : ",sentences1)
print("Sentence 2 : ",sentences2)

print("Consine Similarity : ")
print(similarity.item())