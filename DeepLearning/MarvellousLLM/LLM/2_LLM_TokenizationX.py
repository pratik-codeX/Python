from transformers import AutoTokenizer

print("Done")
#Load pretrained Tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")

sentence = "Python is easy programming language I love it"

#convert the sentence into tokens
tokens = tokenizer.tokenize(sentence)

token_ids = tokenizer.encode(
    sentence,
    add_special_tokens = False
)

# Convert Toekn ids back to text
decoded = tokenizer.decode(token_ids)

print("Original Sentence : ",sentence)

print("Tokens : ",tokens)

print("Tokens IDs :",token_ids)

print("Decoded sentence : ",decoded)