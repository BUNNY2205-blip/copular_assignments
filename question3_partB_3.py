import sqlite3
conn = sqlite3.connect('college.db')
conn.execute('''
Create table student_details(
st_id integer primary key autoincrement,
st_name varchar(100),
st_year integer,
st_city varchar(100),
st_age integer
)
''')
conn.close()
#table 3