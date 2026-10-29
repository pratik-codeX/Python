#-----------------------------------------------------------------
#   Deep Learning PipeLine (DL ops)
#----------------------------------------------------------------
# 1. Read the Data from CSV
# 2. Data Analysis(EDA)
# 3. Preprocessing
# 4. Train Test Split
# 5. Feature Scaling
# 6. FNN Model training
# 7. Model Evaluation
# 8. Graphical Representation   (H.W)
# 9. Model Preserve
# 10. Model loading and Preserve
# 11. Test unseen data
#-----------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#-----------------------------------------------------------------
# 1. Read the Data from CSV
#-----------------------------------------------------------------

print("1. Read the Data from CSV")

data = pd.read_csv("./placement_data.csv")
print(data)

#-----------------------------------------------------------------
# 2. Data Analysis(EDA)
#-----------------------------------------------------------------

print("2. Data Analysis(EDA)")

print("First 5 rows : ")
print(data.head())

print("Columns Names : ")
print(data.columns)

print("Shape of Dataset : ")
print(data.shape)

print("Statistical Summary : ")
print(data.describe())

#-----------------------------------------------------------------
# 3. Preprocessing
#-----------------------------------------------------------------

print("-----------------3. Preprocessing---------------")

# Dataset is Ok there are no null or empty cells

X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y = data['Placed']

print("Input Features : ")
print(X.head())

print("Target : ")
print(Y.head())

#-----------------------------------------------------------------
# 4. Train Test Split
#-----------------------------------------------------------------

print("----------4. Train Test Split---------------")

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.30,random_state=42)

print("Training input shape ")
print(X_train.shape)

print("Testing input shape ")
print(X_test.shape)

print("Training output shape ")
print(Y_train.shape)

print("testing output shape ")
print(Y_test.shape)

#-----------------------------------------------------------------
# 5. Feature Scaling
#-----------------------------------------------------------------

print("5. Feature Scaling")

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

print("Scalled training data : ")

print(X_train_scaled[:5])

#-----------------------------------------------------------------
# 6. FNN Model training
#-----------------------------------------------------------------

print("6. FNN Model training")

model = MLPClassifier(
                        hidden_layer_sizes=(8,4),
                        activation='relu',
                        solver='adam',
                        max_iter=1000,
                        random_state=42
)

print(model)

print("Train the Model")

model.fit(X_train_scaled,Y_train)

print("Model Training Completed")


#-----------------------------------------------------------------
#  7. Model Evaluation 
#-----------------------------------------------------------------

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test,y_pred)

print("Accuracy is : ",accuracy)

cm = confusion_matrix(Y_test,y_pred)

print("Confusion Matrix : ",cm)

print("Predict the probability : ")

Y_prob = model.predict_proba(X_test_scaled)

print(Y_prob[:5])

#-----------------------------------------------------------------
#  8. Graphical Representation Ghari kra
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#  9. Model Preserve
#-----------------------------------------------------------------

print("9. Model Preserve")

joblib.dump(model,"placement_fnn_model.pkl")
joblib.dump(scaler,"placement_scaler.pkl")

print("Model and Scaler gets dump succesfully")

#-----------------------------------------------------------------
#  10. Model loading and Preserve
#-----------------------------------------------------------------

print("10. Model loading and Preserve")

loaded_model = joblib.load("./placement_fnn_model.pkl")
loaded_scaler = joblib.load("./placement_scaler.pkl")

print("Model gets Loaded Succesfully")

#-----------------------------------------------------------------
# 11. Test unseen data
# Aptitude:         70
# Coding :          75
# Communication :   80
# Academics :       85
# Internship :      1
#-----------------------------------------------------------------

new_student = pd.DataFrame([[70,75,80,85,1]],columns =['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scaler.transform(new_student)

new_predication = loaded_model.predict(new_student_scaled)

new_probability = loaded_model.predict_proba(new_student_scaled)

print("New Student data : ")
print(new_student)

print("Prediction Probability : ",new_probability)

if new_predication[0] == 1:
    print("prediction : Placed")
else: 
    print("Prediction : Not Placed")