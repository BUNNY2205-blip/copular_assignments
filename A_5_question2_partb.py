#formation of a data frame with a dictionary
import pandas as pd
data = {
"city":['Jaipur','Ajmer','Udaipur','Jodhpur'],
"radius":[22,33,44,55]
}
myvar = pd.DataFrame(data)
print(myvar)
