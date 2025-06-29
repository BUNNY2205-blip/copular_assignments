import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3], [4, 9, 5]])
arr2 = np.array([[1, 1, 1], [1, 1, 1]])

# 1. Maximum value
print("Max value:", np.max(arr))

# 2. Minimum value
print("Min value:", np.min(arr))

# 3. Number of rows and columns
rows, cols = arr.shape
print("Rows:", rows, "Columns:", cols)

# 4. Select all elements (print one by one)
print("All elements:")
for row in arr:
    for val in row:
        print(val, end=' ')
print()

# 4.1 Specific element (e.g., row 1, column 2)
print("Specific element arr[1][2]:", arr[1][2])

# 5. Sum of all values using for loop
total = 0
for row in arr:
    for val in row:
        total += val
print("Sum using loop:", total)

# 6. Arithmetic operations
print("Addition:\n", arr + arr2)
print("Subtraction:\n", arr - arr2)
print("Multiplication:\n", arr * arr2)
print("Division:\n", arr / arr2)
