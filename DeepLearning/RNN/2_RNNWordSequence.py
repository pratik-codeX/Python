sentance = "food was not good"

words = sentance.split()    #java = split(" ") (" " is delimiter)

for index , word in enumerate(words):
    print("Position ",index+1,":",word)