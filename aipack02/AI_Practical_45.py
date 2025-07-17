import numpy as np

# Load the image data
X = [
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]]),
    np.array([[19, 20, 21], [22, 23, 24], [25, 26, 27]])
]
print("Original X = \n", X)
X = np.array(X)
print("Upgraded numpy X = \n",X)

print("Before Reshape X.shape = \n", X.shape)
# Reshape the data to a consistent shape
X = X.reshape(-1, 3, 3, 1)

# Print the shape of the data
print("After Reshape X.shape = \n", X.shape)
print("After Reshape X = \n", X)