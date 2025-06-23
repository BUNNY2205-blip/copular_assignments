#inserting into the table 2
import sqlite3
conn = sqlite3.connect('college.db')
ins = '''
insert into student_marks(st_id,st_name,st_grade,st_rank)
values('101','ram','B','23'),
('102','shyam','A','2'),
('103','ghanshyam','D','45')
'''
conn.execute(ins)
conn.commit()
conn.close()