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
#   Function Name : SplitData
#   Description   : It performs Split Activity
#   Input         : DataFrame
#   Output        : 4 Subset for Training and Testing
#   Author        : Pratik Nanaso Raut
#   Date          : 16/8/2026
#---------------------------------------------------------

# Step 3 : Split Data

def SplitData(df):
    X = df.drop("Survived",axis = 1)
    Y = df["Survived"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Dataset Spliting Completed Successfully")

    return X_train, X_test, Y_train, Y_test


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

    #step 3
    X_train,X_test,Y_train,Y_test = SplitData(df)

    

if __name__ == "__main__":
    main()