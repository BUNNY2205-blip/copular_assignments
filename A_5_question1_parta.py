#panda series with dictionary
import pandas as pd
dict = {"city1":'Jaipur',"city2":'Ajmer',"city3":'Udaipur',"city4":'Jodhpur'}
print("The dictionary is::")
print(dict)
print("Panda series is::")
my_var = pd.Series(dict)
print(my_var)