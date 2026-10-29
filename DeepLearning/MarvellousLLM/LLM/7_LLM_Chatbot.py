from ollama import chat 

messages = [
    {
        "role":"system",
        "content": "You are a Python programming teacher"
    }
]

print("Marvellous Python Tutor")
print("Type exit to stop")

while True:
    #Accept user input
    print("-"*40)
    Question = input("\n You : ").strip()

    #Stop chatbot
    if Question.lower() == "exit":
        print("Thank you for using Marvellous Bot")
        break

    #ignore empty line
    if not Question:
        continue

    messages.append(
        {
            "role" : "user",
            "content": Question
        }
    )

    response = chat(
        model = "llama3.2:1b",
        messages=messages
    )

    answer = response.message.content

    print("Marvellous AI : ",answer)

    messages.append({
        "role" : "assistant",
        "content": answer
    })