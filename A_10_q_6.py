import numpy as np

A = np.array([[1, -2, 3],
              [-1, 3, -1],
              [2, -5, 5]])

B = np.array([9, -6, 17])

A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)

print("Solution [x, y, z]:")
print(X)
