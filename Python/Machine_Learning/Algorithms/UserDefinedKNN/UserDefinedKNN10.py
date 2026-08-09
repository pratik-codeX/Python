import pandas as np
import math

def MarvellousEucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2+(P1['Y'] - P2['Y'])**2)

    return Ans

def MarvellousKNNClassifier(k = 3):
    Border = "*"*50

    Data = [
        {'point':'A','X':1,'Y': 2,'lable':'Red'},
        {'point':'B','X':2,'Y': 3,'lable':'Red'},
        {'point':'C','X':3,'Y': 1,'lable':'Blue'},
        {'point':'D','X':5,'Y': 6,'lable':'Blue'},
        {'point':'E','X':6,'Y': 6,'lable':'Blue'},
        {'point':'F','X':3,'Y': 4,'lable':'Red'},
        {'point':'G','X':3,'Y': 2,'lable':'Red'},
    ]

    print(Border)
    print("             Marvellous KNN Classifier")
    print(Border)

    for i in Data:
        print(i)

    print(Border)

    new_point = {'X':3 ,'Y':3}

    print("Distances of All points")
    print(Border)
    for d in Data:
        d['distance'] = MarvellousEucDistance(d,new_point)
    print(Border)
    #Result = MarvellousEucDistance(Data[0],new_point)

    for d in Data:
        print(d['distance'],d['lable'])

    print(Border)

    sorted_data = sorted(Data,key = lambda item : item['distance'])

    print("Sorted Data : ")
    print(Border)
    for d in sorted_data:
        print(d)

    print(Border)

    nearest = sorted_data[:k]

    print(Border)
    print("Nearest 3 members are :")
    print(Border)

    for d in nearest:
        print(d)

    print(Border)

    # Voting
    Votes = {}

    for neighbours in nearest:
        label = neighbours['lable']
        Votes[label] = Votes.get(label,0) + 1

    print(Border)
    print("Voting Result is : ")    
    print(Border)

    for d in Votes:
        print("Name : ",d,"Number of votes : ",Votes[d])

    print(Border)

    iMax = 0
    Name = ""

    for d in Votes:
        if (Votes[d] > iMax):
            iMax = Votes[d]
            Name = d

    print("Final Prediction is : ",Name)
def main():
    MarvellousKNNClassifier(5)

if __name__ == "__main__":
    main()