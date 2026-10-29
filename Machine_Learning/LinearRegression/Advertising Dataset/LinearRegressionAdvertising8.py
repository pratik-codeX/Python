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

    ##################################################
    # Step 4 : Statistical Summary (EDA)
    ##################################################
    
    print(Boarder)
    print("Step 4 : Statistical Summary (EDA)")
    print(Boarder)

    print(df.describe())

    print(Boarder)

    ##################################################
    # Step 5 : Co-relation (EDA)
    ##################################################
        
    print(Boarder)
    print("Step 5 : Co-relation (EDA)")
    print(Boarder)

    print(df.corr())

    ##################################################
    # Step 6 : Seperate Dependent and Independent Variables
    ##################################################
            
    print(Boarder)
    print("Step 6 : Seperate Dependent and Independent Variables")
    print(Boarder)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independent Variables : ")
    print(X.head())

    print("Dependent Variables : ")
    print(Y.head())


    #####################################################
    # Step 7 : Split Dependent and Independent Variables
    #####################################################
                
    print(Boarder)
    print("Step 7 : Split Dependent and Independent Variables")
    print(Boarder)

    X_train,X_test,Y_train,Y_test = train_test_split(
                                                    X,
                                                    Y,
                                                    test_size=0.2,
                                                    random_state=42
                                                    )

    print("Training Data : ",X_train.shape)
    print("Testing Data : ",X_test.shape)

    #####################################################
    # Step 8 : Create and train the model
    ######################################################
                    
    print(Boarder)
    print("Step 8 : Create and train the model")
    print(Boarder)

    model = LinearRegression()

    model = model.fit(X_train,Y_train)

    print("Model Trained Successfully...")    

    #####################################################
    # Step 9 : test the model
    ######################################################
                        
    print(Boarder)
    print("Step 9 : test the model")
    print(Boarder)

    Y_pred = model.predict(X_test)

    print("Expected Answers : ")
    print(Y_test[:3])

    print("Predicted Answers : ")
    print(Y_pred[:3])

    #####################################################
    # Step 10 : Evaluate the model
    ######################################################
                            
    print(Boarder)
    print("Step 10 : Evaluate the model")
    print(Boarder)


    MSE = mean_squared_error(Y_test,Y_pred)     #Mean Square Error

    RMSE = np.sqrt(MSE)                         #Root Mean Square Error

    R2 = r2_score(Y_test,Y_pred)

    print("MSE : ",MSE)
    print("RMSE : ",RMSE)
    print("R2 : ",R2)

    #####################################################
    # Step 11: Display Coefficient
    ######################################################
                                
    print(Boarder)
    print("Step 11: Display Coefficient")
    print(Boarder)

    print("TV Coefficient : ",model.coef_[0])
    print("radio Coefficient : ",model.coef_[1])
    print("newspaper Coefficient : ",model.coef_[2])

    print("Intercept : ",model.intercept_)
    
    
def main():

    MarvellousRegression("./Advertising.csv")

if __name__ == "__main__":
    main()