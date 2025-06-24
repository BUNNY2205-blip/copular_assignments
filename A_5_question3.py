import pandas as pd

# Create DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Math": [85, 58, 95, 45, 76],
    "English": [78, 64, 90, 55, 80],
    "Science": [92, 72, 88, 60, 85]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 1) Different ways to iterate over rows
print("\nUsing iterrows():")
for index, row in df.iterrows():
    print(f"{row['Name']} scored {row['Math']} in Math")

print("\nUsing itertuples():")
for row in df.itertuples(index=False):
    print(f"{row.Name} got {row.Science} in Science")

# 2) Selecting rows based on conditions
print("\nStudents with Math > 80:")
print(df[df["Math"] > 80])

# 3) Select any row using iloc[]
print("\n3rd row using iloc:")
print(df.iloc[2])

# 4) Limited row selection with given column
print("\nFirst 3 student names:")
print(df.loc[0:2, "Name"])

# 5) Drop rows based on condition (Math < 40)
print("\nDropping students with Math < 40:")
df_dropped = df[df["Math"] >= 40]
print(df_dropped)

# 6) Insert row at a given position (e.g. index 2)
new_row = {"Name": "Farah", "Math": 88, "English": 77, "Science": 90}
df1 = df.iloc[:2]
df2 = df.iloc[2:]
df = pd.concat([df1, pd.DataFrame([new_row]), df2], ignore_index=True)
print("\nDataFrame after inserting new row at index 2:")
print(df)

# 7) Create list from rows
row_list = df.values.tolist()
print("\nList of rows (each row as list):")
print(row_list)
