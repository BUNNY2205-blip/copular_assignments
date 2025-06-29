#merging two arrays -> a. one d , b. two d
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("First array is::")
print(a)
print("Second array is::")
print(b)
#now we will be concatinating them, but we cannot two arrays of different dimensions so we will reshape first
c = b.reshape(10)
res = np.concatenate((a,c),axis=0)
print(res)
