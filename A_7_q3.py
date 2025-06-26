import pandas as pd

# 1. Load the CSV file
df = pd.read_csv('alcohol.csv')

# 2. Show basic info
print("Initial Dataset Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head(5))

# 3. Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# 4. Clean the data by dropping rows with any missing values
clean_df = df.dropna()
print("\nData after dropping missing values:")
print(clean_df.info())

# 5. Print basic stats
print("\nStatistical Summary:")
print(clean_df.describe())

# 6. Show top and bottom rows
print("\nFirst 10 Rows:")
print(clean_df.head(10))

print("\nLast 10 Rows:")
print(clean_df.tail(10))

# 7. Print shape and column names
print("\nShape of Cleaned DataFrame:")
print(clean_df.shape)

print("\nColumn Names:")
print(clean_df.columns)

# 8. Access a specific column (if exists)
if 'UNITS' in clean_df.columns:
    print("\n'UNITS' Column Data:")
    print(clean_df['UNITS'])

# 9. Optional: Grouped Analysis (e.g., Avg units per category)
if 'CATEGORY' in clean_df.columns and 'UNITS' in clean_df.columns:
    print("\nAverage Units per Category:")
    print(clean_df.groupby('CATEGORY')['UNITS'].mean())

# 10. Optional: Top 5 rows by UNITS
if 'UNITS' in clean_df.columns:
    print("\nTop 5 entries by 'UNITS':")
    print(clean_df.sort_values('UNITS', ascending=False).head(5))
