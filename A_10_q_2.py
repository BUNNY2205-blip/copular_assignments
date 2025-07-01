import numpy as np

# Creating a 3D array of shape (2, 3, 4)
arr = np.random.randint(1, 10, size=(2, 3, 4))
print("Original array shape:", arr.shape)
print("Original array:\n", arr)

# Moving axis 0 to position 2
moved = np.moveaxis(arr, 0, 2)
print("\nAfter moving axis 0 to 2:")
print("New shape:", moved.shape)
print("Modified array:\n", moved)
