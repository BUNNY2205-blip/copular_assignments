import sqlite3
conn = sqlite3.connect('college.db')
conn.execute(''' 
Create table student(
st_id integer primary key autoincrement,
st_name varchar(100),
st_year integer,
st_email varchar(100))
''')
conn.close()
#table 1