import sqlite3
conn = sqlite3.connect('college.db')
data = conn.execute("select* from student_marks where st_grade='A'")
for i in data:
    print(i)
conn.close()