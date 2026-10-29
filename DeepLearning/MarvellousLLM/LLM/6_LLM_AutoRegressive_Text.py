from transformers import pipeline

#Load pretrained text generation pipeline
gererator = pipeline(
    "text-generation",
    model = "distilgpt2"
)

# input prompt
prompt = "Artificial intelligence is"

# generate text
result = generator(
    prompt,
    max_new_tokens = 30,
    do_sample = False,
    pad_token_id = gererator.tokenizer.eos_token_id
)

print("Generated test : ")
print(result[0]["generated_text"])