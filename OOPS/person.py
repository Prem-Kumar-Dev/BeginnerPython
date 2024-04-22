class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def __age__(self):
        return 2024-int(self.dob[2])
    
b=input("Name:")
c=input("Country:")
d=input("DOB:").split("/")
p=person(b,c,d)
a=p.__age__()
print(a)