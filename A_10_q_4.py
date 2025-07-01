import numpy as np
import pandas as pd
a = np.array([1, 2, -3, -4, -5, 6, 7, 8, 9])
print("The given array is:")
print(a)
s = pd.Series(a)
s = s.replace(to_replace=s[s < 0], value=0)
a = s.to_numpy()
print("Array after replacing negative values with 0:")
print(a)
