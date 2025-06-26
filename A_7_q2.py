import pandas as pd
import numpy as np

# 1. Create a date range starting from a specific date
print(" Date Range (Daily):")
date_range = pd.date_range('22/03/2005', periods=10, freq='D')
print(date_range)

# 2. Create a sample DataFrame with string dates
data = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D'],
    'Date': ['22-3-2005', '23-4-2007', '12-12-2001', '23-7-2002']
}, index=[1, 2, 3, 4])

# 3. Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
print("\n🔹 Converted Date Column:")
print(data)

# 4. Extract datetime components
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day
data['Weekday'] = data['Date'].dt.day_name()
print("\n Extracted Components (Year, Month, Day, Weekday):")
print(data)

# 5. Get current timestamp and date
print("\n Current Timestamp:")
print(pd.Timestamp.now())

print("\nToday's Date:")
print(pd.to_datetime("today"))

# 6. Add 5 days to each date (Timedelta operation)
data['Date_plus_5'] = data['Date'] + pd.Timedelta(days=5)
print("\nDate + 5 Days:")
print(data[['Name', 'Date', 'Date_plus_5']])

# 7. Calculate difference from today
today = pd.to_datetime("today")
data['Days_Since'] = (today - data['Date']).dt.days
print("\nDays Since Each Date:")
print(data[['Name', 'Date', 'Days_Since']])

# 8. Resampling example (using a time series)
print("\nResampling Example:")
ts = pd.Series(np.random.randint(10, 100, 100),
               index=pd.date_range("2023-01-01", periods=100, freq='D'))
monthly_avg = ts.resample('M').mean()
print(monthly_avg)
