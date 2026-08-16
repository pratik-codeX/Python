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
#   Function Name : main
#   Description   : Entry Point funcation 
#   Input         : None
#   Output        : None
#   Author        : Pratik Nanaso Raut
#   Date          : 16/8/2026
#---------------------------------------------------------
def main():
    LoadData("./MarvellousTitanicDataset.csv")
    

if __name__ == "__main__":
    main()