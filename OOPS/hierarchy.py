class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class employee(person):
    def __init__(self, name, age, empid, dept):
        self.empid = empid
        self.dept = dept
        person.__init__(self, name, age)

    def display(self):
        print("Name:{} Age:{} Empid:{} Dept:{}".format(self.name, self.age, self.empid, self.dept))

class student(person):
    def __init__(self, name, age, rollno, course):
        self.rollno = rollno
        self.course = course
        person.__init__(self, name, age)

    def display(self):
        print("Name:{} Age:{} Rollno:{} Course:{}".format(self.name, self.age, self.rollno, self.course))


e=employee("Prem", 19, 101, "CSE")
e.display()
s=student("Swastik", 19, 1, "Science")
s.display()
