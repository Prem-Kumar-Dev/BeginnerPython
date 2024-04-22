class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

class employee(person):
    def __init__(self, name, age, empid, dept):
        self.empid = empid
        self.dept = dept
        person.__init__(self, name, age)

class manager(employee):
    def __init__(self, name, age, empid, dept, title):
        self.title = title
        employee.__init__(self, name, age, empid, dept)
    def display(self):
        print("Name:{} Age:{} Empid:{} Dept:{} Title:{}".format(self.name, self.age, self.empid, self.dept, self.title))

m = manager("Swastik", 19, 101, "CSE", "Manager")
m.display()