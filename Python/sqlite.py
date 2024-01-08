import sqlite3
from test2 import Employees
con=sqlite3.connect('student.db')

c=con.cursor()

'''c.execute("""CREATE TABLE employees(
            first text,
            last text,
            pay integer
            )""")'''



emp_1=Employees('John','Doe',80000)
emp_2=Employees('Jame','Doe',80000)
print(emp_1)
'''c.execute("INSERT INTO employees VALUES ('Mary','Schafer',50000)")

con.commit()'''

c.execute("SELECT * FROM employees WHERE last='Schafer'")

print(c.fetchall())

con.commit()

con.close()



