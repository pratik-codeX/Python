from sentence_transformers import SentenceTransformer

# Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentence = [
  "Python is a programming language",
  "Python is used for data science",
  "I support indian criket team"
]

embeddings = model.encode(sentence)

#display sentence embeddings
for index, embedding in enumerate(embeddings):
  print("-"*40)
  print("\n Sentence :",sentence[:10])

  print("Embedding : ")
  print(embedding)

  print("Total dimention : ",len(embedding))