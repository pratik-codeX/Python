sentenses = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels = [1,0,0]        #labels i.e. sentiments

for sentenses,label in zip(sentenses,labels):
    sentiment = "Positive" if label == 1 else "Negative" 
   
    print("Sentense : ",sentenses)
    print("label : ",label)
    print("Meaning :",sentiment)
    print("-------------------------")