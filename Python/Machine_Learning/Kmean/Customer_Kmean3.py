import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

import numpy as np



def main():
    #Step 1 : Load the Data

    df = pd.read_csv("./Mall_Customers.csv")

    print("Dataset loaded with values")
    print(df.head)

    print("Missing values")
    print(df.isnull().sum())

    # Step 2 : Features Selection
    X = df[["AnnualIncome","SpendingScore"]]

    print("Selcted Features\n")

    print(X.head)

    # Step 3 : Scale the data
    scalar = StandardScaler()

    X_scaled = scalar.fit_transform(X)

    print("Scaled data : ")
    print(X_scaled[:5])
    

if __name__ == "__main__":
    main()