#panda series from list
import pandas as pd
fruits = ["mango","bnana","apple","litchi"]
print("The list is::")
print(fruits)
my_var = pd.Series(fruits)
print("Pandas series made from list is::")
print(my_var)