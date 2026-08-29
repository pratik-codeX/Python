import numpy as np

# Step 1 : Define Input Features as X
#                 [x1,x2,x3]
input = np.array([2.0,3.0,4.0])
print("X : ",input)

# step 2 : Define Weight ie. W 
#                   [w1,w2,w3]
weights = np.array([0.5,0.3,0.2])
print("W : ",weights)

# Step 3 : Define Bias
bias = 1.0
print("b : ",bias)

# Step 4 : Calculate Weighted Sum ie. Z
# z = x1w1 + x2w2+ x3w3 + b
# z = (2.0*0.5)+(3.0*0.3)+(4.0*0.2)+1.0

z = np.dot(input,weights) + bias
print("Z :",z)

# Step 5 : Activation function(ReLU)

def ReLU(x):
    return max(0,x)

# Step 6 : Final Output
Y = ReLU(z)
print("Y : ", Y)