words = ["food","was","not","good"]

hidden_state = "empty memory"
 
print("Input Tokens :",words)

print("Initial Hidden state :" , hidden_state)

for index, word in enumerate(words):
    print("Timestep : ",index)
    print("Current word :",word)
    print("Previous memory : ",hidden_state)
    
    hidden_state = "Memory after reading :" + " ".join(words[:index + 1]) + ""
    print("Updated memory : ",hidden_state)
    
    print("--"*30)
