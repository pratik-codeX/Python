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

    ##########################################################
    #   Step 3 : Seperate Independent and Dependent Variables
    ##########################################################
    
    print(Boarder)
    print("Step 3 : Seperate Independent and Dependent Variables : ")
    print(Boarder)

    X = df.drop(columns='Class')
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Boarder)
    print("Input Columns : ",X.columns.to_list)
    print("Output Columns : Class")

    ##########################################################
    #   Step 4 : Spit the Dataset for training and testing
    ##########################################################
    
    print(Boarder)
    print("Step 4 : Spit the Dataset for training and testing : ")
    print(Boarder)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(Boarder)
    print("Details of training and Testing of data")
    print("shape of X_train:",X_train.shape)
    print("shape of X_test:",X_test.shape)
    print("shape of Y_train:",Y_train.shape)
    print("shape of Y_test:",Y_test.shape)
    print(Boarder)

    ##########################################################
    #   Step 5 : Feature Scalling 
    ##########################################################
    
    print(Boarder)
    print("Step 5 : Feature Scalling ")
    print(Boarder)

    scalar = StandardScaler()

    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Feture Scalling Done")
    print(Boarder)

    ##########################################################
    #   Step 6 : Hyper Parameter tuning 
    ##########################################################
    
    print(Boarder)
    print("Step 6 : Hyper Parameter tuning")
    print(Boarder)  

    accuracy_scores = []
    k_values = range(1,21)

    for k in k_values:
        model = KNeighborsClassifier(n_neighbors=5)

        model = model.fit(X_train_scaled,Y_train)

        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print("Accuracy Scores : ")

    for no in accuracy_scores:
        print(no)

    print(Boarder)

    print(Boarder)
    print("Graphical Representation")
    print(Boarder)

    plt.figure(figsize=(8,5))

    plt.plot(k_values,accuracy_scores,marker = "o")
    plt.title("K values vs Accuracy ")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(k_values))
    plt.show()
    
def main():
    MarvellousClassifier("./WinePredictor.csv")

if __name__ == "__main__":
    main()