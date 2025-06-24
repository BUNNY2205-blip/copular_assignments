#as a list of dictionaries
import pandas as pd
data = [
    {"City": "Jaipur", "Radius": 22},
    {"City": "Ajmer", "Radius": 33},
    {"City": "Udaipur", "Radius": 44},
    {"City": "Jodhpur", "Radius": 55}
]
df = pd.DataFrame(data)

print(df)
