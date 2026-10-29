import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#---------------------------------------------------------
#   Function Name : LoadData
#   Description   : Load the Data from CSV  
#   Input         : Name of CSV File
#   Output        : Data Frame
#   Author        : Pratik Nanaso Raut
#   Date          : 16/8/2026
#---------------------------------------------------------

# Step 1 : Load the Data

def LoadData(filename):
    df = pd.read_csv(filename)

    print("Dataset loaded succesfully")
    print(df.head())

    return df

#---------------------------------------------------------
#   Function Name : Preprocess
#   Description   : It performs Data Analysis(Exploratory Data Analysis)
#   Input         : DataFrame
#   Output        : Updated DataFrame
#   Author        : Pratik Nanaso Raut
#   Date          : 16/8/2026
#---------------------------------------------------------

# Step 2 : Data Preprocessing

def Preprocess(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
        ],
        errors = "ignore"
        )

    # Handle missing Values 
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    #Convert Categorical to numeric data    
    df = pd.get_dummies(                                        #one hot encoding
        df, 
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )

    print(df.head())

    print("Data Preprocessing Completed")

    return df

#---------------------------------------------------------
#   Function Name : main
#   Description   : Entry Point funcation 
#   Input         : None
#   Output        : None
#   Author        : Pratik Nanaso Raut
#   Date          : 16/8/2026
#---------------------------------------------------------
def main():
    # Step 1 
    df = LoadData("./MarvellousTitanicDataset.csv")

    #step 2 
    df = Preprocess(df)

if __name__ == "__main__":
    main()