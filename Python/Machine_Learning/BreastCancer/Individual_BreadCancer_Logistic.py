import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#------------------------------------------------------
#   Step 1: Load the dataset
#-------------------------------------------------------

df = pd.read_csv("./breast_cancer.csv")

print("Shape of dataset is : ",df.shape)

print("First few rows : ")
print(df.head())

#-------------------------------------------------------
#   Step 2: Load the dataset
#-------------------------------------------------------

X = df.drop("target",axis = 1)
Y = df["target"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

#-------------------------------------------------------
#   Step 3: Split dataset for training and testing 
#-------------------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(
                                                X,
                                                Y,
                                                test_size=0.2,
                                                random_state=42
                                            )

#-------------------------------------------------------
#   Step 4: Scale the features 
#-------------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

#-------------------------------------------------------
#   Step 5: Create the model 
#-------------------------------------------------------

model = LogisticRegression(max_iter=1000)

#-------------------------------------------------------
#   Step 6: Train the model 
#-------------------------------------------------------

model = model.fit(X_train,Y_train)

#-------------------------------------------------------
#   Step 7: Test the model 
#-------------------------------------------------------

Y_pred = model.predict(X_test)

#-------------------------------------------------------
#   Step 8: Evaluate the model 
#-------------------------------------------------------

print("Accuracy : ",accuracy_score(Y_test,Y_pred) * 100)

print("Confusion Matrix : ",confusion_matrix(Y_test,Y_pred))