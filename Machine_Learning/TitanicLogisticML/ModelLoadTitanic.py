import pandas as pd
import joblib

def LoadModel(Filename):
    model = joblib.load(Filename)

    print("Model Loaded Succesfully")

    print(model.feature_names_in_)

    return model

def PredictPassenger(model):
    print("Enter the Information ")

    Pclass = int(input("Enter Pclass (1/2/3)"))
    Sex = int(input("Enter Sex : (0 : M / 1 : F)"))
    Age = float(input("Enter Age : "))
    sibsp = int(input("Enter sibsp : "))    #sibling and spous
    Parch = int(input("Enter Parch : "))
    Fare = int(input("Enter Fare : "))
    Embarked = float(input("Enter embarke : (0/1/2)"))
    Passengerid = 0
    zero = 0

    passenger = pd.DataFrame([{
        "Pclass": Pclass,
        "Sex" : Sex,
        "Age" : Age,
        "sibsp":sibsp,
        "Parch":Parch,
        "Fare":Fare,
        "Passengerid":Passengerid,
        "zero" : zero,
        "Embarked_1.0": 1 if Embarked == 1 else 0,
        "Embarked_2.0": 1 if Embarked == 2 else 0
    }])

    passenger = passenger[model.feature_names_in_]

    result = model.predict(passenger)

    if result == 1:
        print("Survived")
    
def main():
    model = LoadModel("./MarvellousTitanic.pkl")

    PredictPassenger(model)
    

if __name__ == "__main__":
    main()