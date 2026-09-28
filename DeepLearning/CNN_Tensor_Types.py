import tensorflow as tf

#scaler tensor (0D tensor)
scalar_tensor = tf.constant(11)

print("Scalar tensor : ",scalar_tensor)

# 1D tensor (vecotr)
vector_tensor = tf.constant(11,21,101)
print("Vector tensor :",vector_tensor)

# 2D tensor (matrix)
matrix_tensor = tf.constant([[10,20,30],[40,50,60]])
print("Matrix Tensor : ",matrix_tensor)

# 3D tensor (2x2x3)
tensor_3d = tf.constant([
    [[1,2],[3,4]],
    [[5,5],[6,6]],
    [[7,8],[9,10]]
])

print("3D tensor",tensor_3d)