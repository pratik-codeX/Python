from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences1 = "I dont like to eat mango"
sentences2 = "I love to play cricket"

embeddings1 = model.encode(sentences1,convert_to_tensor = True)
embeddings2 = model.encode(sentences2,convert_to_tensor = True)

# calculate cosine similarity
similarity = util.cos_sim(embeddings1,embeddings2)

print("Sentence 1 : ",sentences1)
print("Sentence 2 : ",sentences2)

print("Consine Similarity : ")
print(similarity.item())