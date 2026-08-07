import pandas as pd

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