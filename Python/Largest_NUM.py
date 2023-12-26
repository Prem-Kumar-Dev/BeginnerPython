"""import array as a

a=a.array('d',[])

while True:
    num=(input("Number OR 'E' to Exit:_"))
    if num=="E"or num=="e":
        break
    a.append(float(num))
    print(a)

b=a[0]
for i in a[1:]:
    if b<i:
        b=i

print(b)

"""
n=0
while True:
    
    num=(input("Number OR 'E' to Exit:_"))

    if num=="E"or num=="e":
        break
    float(num)
    if n==0 and n!="E" and n!='e':
        b=num
    elif b<num:
            b=num
    n=n+1
    
print(b)
