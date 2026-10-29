sentenses = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels = [1,0,0]        #labels i.e. sentiments

for sentenses,label in zip(sentenses,labels):
    print("Sentense : ",sentenses)
    print("label : ",label)

    if label == 1:
        print("Meaning : Positive sentiment")
    else:
        print("Meaning : Negative sentiment")

    print("-------------------------")