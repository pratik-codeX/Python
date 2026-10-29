import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Boarder = "-"* 30
##################################################
#   Step 1 : Load the Data set
##################################################

print(Boarder) 
print("Step 1 : Load the dataset")
print(Boarder) 

Datapath = "./iris.csv"

df = pd.read_csv(Datapath)

print("Dataset Loaded Successfully")

print("Initial Entries from dataset are :",df.head())

##################################################
#   Step 2 : Data Analysis (EDA) Exploratory Data Analysis
##################################################

print(Boarder)
print("Step 2 : Data Analysis (EDA)")
print(Boarder)

#Shape of Dataset

print("Shape of dataset :",df.shape)

print("Columns names : ",list(df.columns))

print("Missing Values per column : ")
print(df.isnull().sum())        #this are canonical function call

print("Class Distribution (species Count)")
print(df["species"].value_counts())

print("Statistical report of dataset :")
print(df.describe())

#########################################################
#   Step 3 : Decide Independent and Dependent variables
#########################################################

print(Boarder)
print("Step 3 : Decide Independent and Dependent variables")
print(Boarder)

# X : Independent Variables / Features
# Y : Dependent Variables   / Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)" ,
    "petal length (cm)",
    "petal width (cm)" 
    ]

X = df[feature_cols]
Y = df["species"]

print("X shape :",X.shape)
print("Y shape :",Y.shape)

#########################################################
#   Step 4 : Visualization of Dataset
#########################################################

print(Boarder)
print("Step 4 : Visualization of Dataset")
print(Boarder)

#
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)

plt.title("Marvellous Iris Case Study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()

#########################################################
#   Step 5 : Split the Dataset for training and testing
#########################################################

print(Boarder)
print("Step 5 : Split the Dataset for training and testing")
print(Boarder)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset splitting activity done")

print("X :",X.shape)    #(150,4)
print("Y :",Y.shape)    #(150,)

print("X_train : ",X_train.shape)   #(75,4)
print("X_test : ",X_test.shape)     #(75,4)

print("Y_train : ",Y_train.shape)   #(75,)
print("Y_test : ",Y_test.shape)     #(75,)

#########################################################
#   Step 6 : Build the model
#########################################################

print(Boarder)
print("Step 6 : Build the model")
print(Boarder)

model = DecisionTreeClassifier(max_depth=5)
print("Model gets Created Successfully")

#########################################################
#   Step 7 : Train the model
#########################################################

print(Boarder)
print("Step 7 : Train the model")
print(Boarder)

model = model.fit(X_train,Y_train)

print("Model Trained Successfully")


#########################################################
#   Step 8 : Evaluate the model
#########################################################

print(Boarder)
print("Step 8 : Evaluate the model")
print(Boarder)

y_pred = model.predict(X_test)

print("Model testing done")

print("Expected Answers :")
print(Y_test)

print("Predicted Answers :")
print(y_pred)