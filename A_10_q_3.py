import numpy as np

# Create a 2D array with some missing (NaN) values
a = np.array([
    [1, 2, 3, np.nan, 5],
    [6, 7, 8, 9, np.nan]
])
print("Original array:")
print(a)
# Calculate the average of each column, ignoring NaN values
col_avg = np.nanmean(a, axis=0)
print("\nColumn-wise averages (ignoring NaN):")
print(col_avg)
# Find the positions of NaN values in the array
nan_positions = np.isnan(a)
# Replace NaNs with the corresponding column averages
a[nan_positions] = np.take(col_avg, np.where(nan_positions)[1])
print("\nArray after replacing NaNs with column averages:")
print(a)
