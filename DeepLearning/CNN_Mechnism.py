import numpy as np

image = np.array([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0], 
    [255,255,255,255,255,255],
    [255,255,255,255,255,255],
    [255,255,255,255,255,255]
])

print("\n Original 6x6 Image")
print(image)

kernel = np.array([
    [-1, -1, -1],
    [ 0, 0, 0],
    [ 1, 1, 1]
])

print("\n3x3 kernel")
print(kernel)

feature_map= np.zeros((4,4))

for i in range(4):
    for j in range(4):
        region = image[i:i+3,j:j+3]

        result = np.sum(region * kernel)

        feature_map[i][j] = result


print("\nFeature map(Detected Edge)")
print(feature_map)