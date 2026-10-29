import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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