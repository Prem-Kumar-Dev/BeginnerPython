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
    if Duplicate_data(roll)==0:
        name=input("Name:")
        maths=float(input("Mark in Maths:"))
        physics=float(input("Mark in Physics:"))
        chemistry=float(input("Mark in Chemistry:"))
        english=float(input("Mark in English:"))
        per=((maths+physics+chemistry+english)/400)*100
        std=StudentPMS(roll,name,maths,physics,chemistry,english)
        c.execute("INSERT INTO Students VALUES (?,?,?,?,?,?,?)", (std.roll,std.name,std.maths,std.physics,std.chemistry,std.english,per))
        con.commit()
    else:
        print("\nThe roll number already exists\n")
        input()

def Search_data():
    # Searching data from the table:
    roll = input("Enter Roll Number to Search:")
    c.execute("SELECT * FROM Students WHERE roll=?", (roll,))
    searchlist = ["Roll:", "Name:", "Maths:", "Physics:", "Chemistry:", "English:","Percentage:"]
    counter=0
    items = c.fetchall()
    if not items:
        print("No data found for the given roll number.")
    else:
        student_info = items[0]
        for item in student_info:
            print(searchlist[counter], item)
            counter+=1
    holder = input("\nPress Enter to continue...")

def Update_data():
    # Updating data to the table:
    roll = input("Roll Number:")
    if Duplicate_data(roll)==0:
        print("No data found for the given roll number.")
    else:
        maths = float(input("Update Mark in Maths:"))
        physics = float(input("Update Mark in Physics:"))
        chemistry = float(input("Update Mark in Chemistry:"))
        english = float(input("Update Mark in English:"))
        per = ((maths+physics+chemistry+english)/400)*100
        c.execute("UPDATE Students SET maths = ?, physics = ?, chemistry = ?, english = ?, percentage = ? WHERE roll = ?", (maths, physics, chemistry, english, per, roll))
        con.commit()
        print("Data updated successfully.")
    holder = input("\nPress Enter to continue...")

def Delete_data():
    #Deleting data from the table:
    roll=input("Enter Roll Number to Delete:")
    c.execute("DELETE FROM Students WHERE roll=?", (roll,))
    con.commit()
    print("Data Deleted successfully.")
    holder = input("\nPress Enter to continue...")

def Table_disp():
    #Displaying table
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
    holder = input("\nPress Enter to continue...")
    
def Duplicate_data(roll):
    #checks duplicate data
    c.execute("SELECT * FROM Students WHERE roll=?", (roll,))
    items = c.fetchall()
    if not items:
        return 0
    else:
        return 1


def main():
    try:
        while True:
            Check_AND_make_table()
            Table_disp()
            user=int(input("Press:\n1) ENTER DATA\n2) SEARCH\n3) UPDATE\n4) DELETE(data)\n5) DELETE(table)\n0) EXIT \n_ "))
            if user==0:
                Table_disp()
                print("Thank You!")
                break
            elif user==1:
                Adding_data()
            elif user==2:
                Search_data()
            elif user==3:
                Update_data()
            elif user==4:
                Delete_data()
            elif user==5:
                Drop_Table()
            else:
                print("Enter a Valid input.")
                holder = input("\nPress Enter to continue...")
            Table_disp()
    except ValueError:
        print("Please enter valid data.")
        holder = input("\nPress Enter to continue...")
        main()
main()
con.close()
