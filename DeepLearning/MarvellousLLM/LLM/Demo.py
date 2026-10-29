from ollama import chat

response = chat(
    model = "llama3.2:1b",
    messages = [
        {
            "role" : "user",
            "content" : "MyName is Pratik ."
        }
    ]
)

print(response.message.content)