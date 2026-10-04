sentense = "food was not good"

words = sentense.split()

print("Actual sentance is : ",sentense)

for index, word in enumerate(words):
    print("TimeStep : ",index+1," : ",word)
