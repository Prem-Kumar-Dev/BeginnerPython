class triangle:

    def __perimeter__(self,a,b,c):
        return a+b+c
    

x,y,z=[int(a) for a in input().split()]

p=triangle()
print(p.__perimeter__(x,y,z))
