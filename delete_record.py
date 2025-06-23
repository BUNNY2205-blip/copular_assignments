import sqlite3
conn = sqlite3.connect('college.db')
print("Your data before deletion::\n")
data = conn.execute("select* from student")
for i in data:
    print(i)
id = int(input("Enter the valid id of the student whoes data you want to delete::"))
conn.execute(f"delete from student where st_id = {id}")
conn.commit()
print("Your data before deletion::\n")
data1 = conn.execute("select*from student")
for i in data1:
    print(i)
conn.close()