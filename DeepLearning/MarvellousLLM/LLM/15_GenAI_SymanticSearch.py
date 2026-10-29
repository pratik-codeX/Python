from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Knowledge Base
documents = [
                "Python is used for Machine Learning",
                "Java is used for enterprise application",
                "SQL is used to manage databases",
                "HTML is used to create web pages",
                "TensorFlow is used for deep learning"             
]

# Generate document embedding
document_embedding = model.encode(documents,convert_to_tensor=True)

# Accept question
query = input("Enter you Quesiton")

# Generate query embedding
query_embedding = model.encode(query,convert_to_tensor=True)

# Calculate similarity
scores = util.cos_sim(query_embedding,document_embedding)[0]

# Display Scores

for index, score in enumerate(scores):
    print(documents[index],":",score.item())
    
# Find the best document
best_index = scores.argmax().item()

print("Most relevant document : ")
print(documents[best_index])

