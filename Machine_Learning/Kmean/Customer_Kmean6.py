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

    # Step 4 : Elbow method

    WCSS = []

    for k in range(1,11):
        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(X_scaled)

        WCSS.append(model.inertia_)

    print("Values of WCSS : ")

    for i in range(len(WCSS)):
        print(f"{i+1} : {WCSS[i]}")


    # Step 5 : Visualize

    plt.plot(range(1,11),WCSS,marker = "o")
    plt.xlabel("Number of cluster : k")
    plt.ylabel("WCSS")  #within cluster sum of square
    plt.title("Mavellous Elbow method")
    plt.grid()
    plt.show()

    # step 6 : Final model

    model = KMeans(
                n_clusters=4,
                random_state=42,
                n_init=10
                )

    cluster = model.fit_predict(X_scaled)

    df["Cluster"] = cluster

    print("Dataset with clusters : ")
    print(df.head(100))


if __name__ == "__main__":
    main()