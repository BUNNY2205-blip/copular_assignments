import sqlite3
conn = sqlite3.connect('college.db')
print("Your data before updation::")
data = conn.execute("select * from student")
for i in data:
    print(i)
conn.execute("update student set st_name='sanchit' where st_id = '103'")
conn.commit()
print("Your data after updation is::")
data1 = conn.execute("select*from student")
for i in data1:
    print(i)
conn.close()

