from ollama import chat

#Select the local LLM
Model = "llama3.2:1b"

# define prompts
prompts = [
    "Explain recurssion", 

    "Explain recurssion in python in 3 simple points",

    """You are experienced python teacher.
        Explain recursion for beginer.
        Give one simple Example.""",

    """Convert programming languages to uppercase.
    Example 1:
    Input : Python
    Output : PYTHON

    Example 2:
    Input : Java
    Output : JAVA

    Example 3:
    Input : Javascript
    Output :"""
]   

# Execute Every Prompt
for index, prompt in enumerate(prompts, start = 1):
    print("-"*30)

    print("prompt number : ",index)
    print("Input Prompt :",prompt)

    response = chat(
        model = Model,
        messages = [
            {
                "role" : "user",
                "content" : prompt
            }
        ]
    )

    print("\n Response from LLM is : ")

    print(response.message.content)