import pandas as pd

# sample data
df = pd.DataFrame({
    'Email': ['john.doe@example.com', 'invalid@com', 'test123@gmail.co.in'],
    'Mobile': ['9876543210', '123456', '8123456789'],
    'Password': ['Welcome123!', 'weakpass', 'Strong@123'],
    'Name': ['Sanchit', 'x', 'JohnDoe']
})

# validate email
df['Valid_Email'] = df['Email'].str.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# validate mobile
df['Valid_Mobile'] = df['Mobile'].str.match(r'^[6-9]\d{9}$')

# validate password
df['Valid_Password'] = df['Password'].str.match(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$'
)

# validate name
df['Valid_Name'] = df['Name'].str.match(r'^[A-Za-z]{2,}$')

print(df)
