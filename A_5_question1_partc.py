#acessing elemetns in a series in pandas
import pandas as pd
dict = {"city1":'Jaipur',"city2":'Ajmer',"city3":'Udaipur',"city4":'Jodhpur'}
print("The dictionary is::")
print(dict)
print("Panda series is::")
my_var = pd.Series(dict)
print(my_var)
#to access elements we can access by labels 
#by position
#by slicing
#using loc
#using iloc
print(my_var['city2'])
print(my_var[0:2])
