#data frame with a list
import pandas as pd

data = [['Jaipur', 22], ['Ajmer', 33], ['Udaipur', 44], ['Jodhpur', 55]]
myvar = pd.DataFrame(data, columns=["city", "radius"])
print(myvar)
