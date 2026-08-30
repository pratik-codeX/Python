import math

def Marvellous_MAE(Y_True,Y_pred):
    n = len(Y_pred)
    total_error = 0

    for i in range(n):
        error = abs(Y_True[i]-Y_pred[i])
        total_error = total_error + error

    MAE = total_error / n

    return MAE

Y_True = [10,20,30]
Y_pred = [12,18,33]

loss = Marvellous_MAE(Y_True,Y_pred)

print("Loss is : ",loss)