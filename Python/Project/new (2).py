import sqlite3
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
import sys

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

def Search_data():
    #Searching data from the table:
    roll=input("Enter Roll Number to Search:")
    c.execute("SELECT * FROM Students WHERE roll=?", (roll,))
    items=c.fetchall()
    for item in items:
        print(item)

def Update_data():
    roll = input("Roll Number:")
    maths = float(input("Update Mark in Maths:"))
    physics = float(input("Update Mark in Physics:"))
    chemistry = float(input("Update Mark in Chemistry:"))
    english = float(input("Update Mark in English:"))
    per = ((maths+physics+chemistry+english)/400)*100
    c.execute("UPDATE Students SET maths = ?, physics = ?, chemistry = ?, english = ?, percentage = ? WHERE roll = ?", (maths, physics, chemistry, english, per, roll))
    con.commit()
    print("Data updated successfully.")

def Delete_data():
    #Deleting data from the table:
    roll=input("Enter Roll Number to Delete:")
    c.execute("DELETE FROM Students WHERE roll=?", (roll,))
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

class StudentPMS_GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student PMS")

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)

        self.add_data_button = QPushButton("Add Data", self)
        self.add_data_button.clicked.connect(Adding_data)

        self.search_data_button = QPushButton("Search Data", self)
        self.search_data_button.clicked.connect(Search_data)

        self.update_data_button = QPushButton("Update Data", self)
        self.update_data_button.clicked.connect(Update_data)

        self.delete_data_button = QPushButton("Delete Data", self)
        self.delete_data_button.clicked.connect(Delete_data)

        self.layout.addWidget(self.add_data_button)
        self.layout.addWidget(self.search_data_button)
        self.layout.addWidget(self.update_data_button)
        self.layout.addWidget(self.delete_data_button)

if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        start_app = True
    else:
        start_app = False
    window = StudentPMS_GUI()
    window.show()
    if start_app:
        app.exec_()
con.close()
