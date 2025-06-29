import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8]])
print("Your 2-d array is::")
print(a)
#now we will convert the 2 d array into 1 d
b = a.reshape(8)
print("Converted array is::")
print(b)
