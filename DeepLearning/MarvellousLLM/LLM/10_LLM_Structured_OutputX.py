from ollama import chat
import json

# Prompt for LLM
prompt = """
                Give me the information about Python programming language.
                Return result as JSON with these keys:
                "language"
                type
                creator
         """
# Execute the LLM
response = chat(
    model = "llama3.2:1b",
    messages = [
      {  "role" : "user",
        "content" : prompt
      }
    ],
    format = "json"
)

print("Response of LLM : ")

print(response.message.content)

answer = response.message.content

# Convert json String to python dictonary
data = json.loads(answer)

print("Data from Dictonary")
print(data)

print("Language :",data.get("language"))
print("Type :",data.get("type"))
print("Creator :",data.get("creator"))