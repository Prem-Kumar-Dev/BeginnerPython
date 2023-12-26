import sqlite3
import os

#Creating Objects to hold all the Student related Variables:
class StudentPMS:
    
    def __init__(self,roll,name,maths,physics,chemistry,english):
        self.roll=roll
        self.name=name
        self.maths=maths
        self.physics=physics
        self.chemistry=chemistry
        self.english=english
        
    

con=sqlite3.connect('studentPMS.db')                   #Creating Sqlite database within memory:
c=con.cursor()

def Check_AND_make_table():
    # Check if the table already exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Students'")
    table_exists = c.fetchone()

    if not table_exists:                              #Creating a Table:
        c.execute("""CREATE TABLE Students(
                roll text,
                name text,
                maths real,
                physics real,
                chemistry real,
                english real,
                percentage real
                )""")
        con.commit()

def Adding_data():
    #Creating data and adding it to table:
    roll=input("Roll Number:")
    name=input("Name:")
    maths=float(input("Mark in Maths:"))
    physics=float(input("Mark in Physics:"))
    chemistry=float(input("Mark in Chemistry:"))
    english=float(input("Mark in English:"))
    per=((maths+physics+chemistry+english)/400)*100
    std=StudentPMS(roll,name,maths,physics,chemistry,english)
    
    c.execute("INSERT INTO Students VALUES (?,?,?,?,?,?,?)", (std.roll,std.name,std.maths,std.physics,std.chemistry,std.english,per))
    con.commit()

def Table_disp():
    os.system('cls')
    c.execute("SELECT * FROM Students ORDER BY percentage DESC")
    items=c.fetchall()
    print("Roll"+"\t\t|NAME"+"\t\t|MATHS"+"\t\t|PHYSICS"+"\t|CHEMISTRY"+"\t|ENGLISH"+"\t|PERCENTAGE")
    print("---------------------------------------------------------------------------------------------------------------")
    for item in items:
        print(str(item[0])+"\t|"+str(item[1])+"\t|"+str(item[2])+"\t\t|"+str(item[3])+"\t\t|"+str(item[4])+"\t\t|"+str(item[5])+"\t\t|"+str(item[6])+"%")
    print("\n\n\n\n")

def Drop_Table():
    #Deleting entire table
    c.execute("DROP TABLE Students")
    con.commit()
    

def main():
    while True:
        Check_AND_make_table()
        Table_disp()
        Adding_data()
        Table_disp()
        user=int(input("Press:\n1) ENTER ANOTHER DATA\n2) SEARCH\n3) UPDATE\n4) DELETE(data)\n5) DELETE(table)\n0) EXIT \n_ "))
        if user==0:
            Table_disp()
            break
        if user==5:
            Drop_Table()
        Table_disp()
main()
con.close()

