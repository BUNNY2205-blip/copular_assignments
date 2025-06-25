#converting series of date strings into time series
import pandas as pd
date = pd.Series(['2025-06-20','2025-06-21','2025-06-22'])
#converting the date series into time series
time = pd.to_datetime(date)
print(time)
