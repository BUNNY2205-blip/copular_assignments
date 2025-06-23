#inserting into the table
import sqlite3
conn = sqlite3.connect('college.db')
ins = '''
insert into student(st_id,st_name,st_year,st_email)
values('101','ram','2','ram@mail'),
('102','shyam','2','shyam@mail'),
('103','ganshyam','3','ganshyam@mail')
'''
conn.execute(ins)
conn.commit()
conn.close()
