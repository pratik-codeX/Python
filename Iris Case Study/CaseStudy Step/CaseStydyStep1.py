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