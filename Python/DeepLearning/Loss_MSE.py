import math

def Marvellous_MSE(Y_True,Y_pred):
    n = len(Y_pred)
    total_error = 0

    for i in range(n):
        error = Y_True[i]-Y_pred[i]
        total_error = total_error+(error**2)

    MSE = total_error / n

    return MSE

Y_True = [10,20,30]
Y_pred = [12,18,33]

loss = Marvellous_MSE(Y_True,Y_pred)

print("Loss is : ",loss)

