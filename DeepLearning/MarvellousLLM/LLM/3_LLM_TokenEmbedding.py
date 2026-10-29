import torch

from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

# pretrained model name
model_name = "distilgpt2"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load pretrained language model 
model = AutoModelForCausalLM.from_pretrained(model_name)

#input sentence 
sentence = "I love AI"

# Convert text into PyTorch tensors
inputs = tokenizer(
    sentence,
    return_tensors = "pt"
)

# Extract token ID
token_ids = inputs["input_ids"]     

#Access the pretrained input embedding layer

embedding_layer = model.get_input_embeddings()

# Retrive the embedding vectors
embeddings = embedding_layer(token_ids)

print("Input Sentence :",sentence)

print("Token IDs : ")
print(token_ids)

print("Embedding Shape : ")
print(embeddings.shape)

print("First token embedding ")
print(embeddings[0,0 :10])