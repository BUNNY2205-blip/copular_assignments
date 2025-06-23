import sqlite3
conn = sqlite3.connect('college.db')
conn.execute('''
Create table student_marks(
st_id integer primary key autoincrement,
st_name varchar(100),
st_grade varchar(5),
st_rank integer
)
''')
conn.close()
#table 2