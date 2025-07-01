import numpy as np
a = np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
print("Youra array is::")
print(a)
#replacing the null values with 0
res = np.nan_to_num(a,copy=True,nan=0)
print("After removing the NAN values::")
print(res)
