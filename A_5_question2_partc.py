#creating a data frame using list of lists
import pandas as pd
data = [['Jaipur', 22], ['Ajmer', 33], ['Udaipur', 44], ['Jodhpur', 55]]
df = pd.DataFrame(data, columns=["City", "Radius"])
print(df)
