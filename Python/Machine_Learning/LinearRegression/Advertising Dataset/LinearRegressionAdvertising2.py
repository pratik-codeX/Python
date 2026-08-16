import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score


def MarvellousRegression(Datapath):

    #################################################
    # Step 1 : Load the Data
    #################################################

    Boarder = "*"*50
    print(Boarder)
    print("Step 1 : Load the Data")
    print(Boarder)

    df = pd.read_csv(Datapath)

    print(df.head())

    #################################################
    # Step 2 : Remove Unwanted Column
    #################################################
    
    print(Boarder)
    print("Step 2 : Remove Unwanted Column")
    print(Boarder)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    ##################################################
    # Step 3 : Check Mission Values (EDA)
    ##################################################

    print(Boarder)
    print("Step 3 : Check Mission Values (EDA)")
    print(Boarder)

    print("Total Missing Values : ")
    print(Boarder)
    print(df.isnull().sum())
    print(Boarder)

    


def main():

    MarvellousRegression("./Advertising.csv")

if __name__ == "__main__":
    main()