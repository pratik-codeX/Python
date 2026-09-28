import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def main():
    #Independent Variables
    X = np.array([
        [1,2],
        [2,3],
        [3,1],
        [5,6]
    ])

    #Dependent Variables
    Y = np.array(["Red","  Red","Blue","Blue"])

    new_point = np.array([[3,3]])

    print("Independent Variables :")
    print(X)

    print("Dependent Variables : ")
    print(Y)

    print("Testing point is : ")
    print(new_point)

if __name__ == "__main__":
    main()