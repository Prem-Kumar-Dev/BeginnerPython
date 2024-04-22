class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class employee:
    def __init__(self,name,age,empid,dept):
        self.empid=empid
        self.dept=dept
        self.name=name
        self.age=age

class student:
    def __init__(self,name,age,rollno,marks):
        self.rollno=rollno
        self.marks=marks
        self.name=name
        self.age=age

class teacher(employee,student):
    def __init__(self,name,age,empid,dept,rollno,marks):
        employee.__init__(self,name,age,empid,dept)
        student.__init__(self,name,age,rollno,marks)
    def display(self):
        print("Name:{} Age:{} Empid:{} Dept:{} Rollno:{} Marks:{}".format(self.name,self.age,self.empid,self.dept,self.rollno,self.marks))


t=teacher("Swastik",19,101,"CSE",1,100)
t.display()