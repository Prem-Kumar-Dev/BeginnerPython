"""import array as arr
a=arr.array('d',[])
while True:
    m=input("The number or 'E' to exit:_")
    if m=="E" or m=="e":
        break
    a.append(float(m))

    print(a)
d,b= 0,a[0]

for c in range(0,len(a)):
    n, pro= 0, len(a)-c    
    for i in a[1:pro]:
        n=n+1
        if n+1==pro:
            if b>i:
                d=a[n]
                a[n]=b
                b=d
            elif c==len(a)-2:
                a[0]=b

        elif b<i:
            a[n]=b
            b=i


print(a)"""

import array as arr
a=arr.array('d',[])
while True:
    m=input("The number or 'E' to exit:_")
    if m=="E" or m=="e":
        break
    a.append(float(m))

    print(a)

for i in range(0,len(a)-1):
    for j in range(0,(len(a)-i)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            print(a)











    

