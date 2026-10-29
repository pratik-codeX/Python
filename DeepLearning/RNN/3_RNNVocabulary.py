sentenses = [
    "food was good",
    "food was bad",
    "food was not good"
]

vocabulory = []

for sentence in sentenses:
    words = sentence.split()

    for word in words:
        if word not in vocabulory:     
           vocabulory.append(word)

for index , x in enumerate(vocabulory):
    print("Position ",index+1,":",x)