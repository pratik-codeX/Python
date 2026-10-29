from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(Datapath):
    Boarder = "-"*40

    ##########################################################
    #   Step 1 : Load the Dataset from CSV File
    ##########################################################
    print(Boarder)
    print("Step 1 : Load the Dataset from CSV File")
    print(Boarder)

    df = pd.read_csv(Datapath)

    print(Boarder)
    print("Some Entries from Dataset : ")
    print(df.head())
    print(Boarder)

    ##########################################################
    #   Step 2 : Clean the Dataset
    ##########################################################
    print(Boarder)
    print("Step 2 : Clean the Dataset : ")
    print(Boarder)

    df.dropna(inplace=True)     #tithlya tith NaN,None and NaT removes krto or missing values

    print("Total Records : ",df.shape[0])
    print("Total Columns :",df.shape[1])
    print(Boarder)

    print("Shape of dataset :",df.shape) 

def main():
    MarvellousClassifier("./WinePredictor.csv")

if __name__ == "__main__":
    main()