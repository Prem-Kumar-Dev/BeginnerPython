class rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __area_rec__(self):
        return self.x*self.y
    
l,b=[int(a) for a in input().split()]

p=rectangle(l,b)
a=p.__area_rec__()
print(a)