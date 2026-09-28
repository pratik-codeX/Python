import pandas as np
import math
def MarvellousEucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2+(P1['Y'] - P2['Y'])**2)

    return Ans

def MarvellousKNNClassifier():
    Border = "*"*50

    Data = [
        {'point':'A','X':1,'Y': 2,'lable':'Red'},
        {'point':'B','X':2,'Y': 3,'lable':'Red'},
        {'point':'C','X':3,'Y': 1,'lable':'Blue'},
        {'point':'D','X':5,'Y': 6,'lable':'Blue'},
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

def main():
    MarvellousKNNClassifier()


if __name__ == "__main__":
    main()