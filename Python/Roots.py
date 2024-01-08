import array as arr
a=float(input("Coefficient of x\u00b2:_"))
b=float(input("Coefficient of x:_"))
c=float(input("Constant:_"))
x=arr.array('d',[a,b,c])
y=arr.array('d',[])
z=arr.array('d',[])
eq=arr.array('d',[])
ans=arr.array('d',[])


midProduct=a*c
factor=2
fac1,fac2 = 0,0

#just to find factors
def factorize():

    global y
    global factor
    global midProduct
    if midProduct<0:
        midProduct=-1*(midProduct)
    while midProduct!=1:

        while midProduct%factor==0:
            y.append(factor)
            midProduct=midProduct/factor
        factor=factor+1

#order of operaitons:
def signCheck():
    global b
    global c

    if b<0 and c>0:
        return 1
    elif b<0 and c<0:
        return 2
    elif b>0 and c>0:
        return 3
    elif b>0 and c<0:
        return 4

#find usable factors:
def factorCheck():
    global a,c
    mid=a*c
    global z
    mid=abs(mid)
    for i in range (1,int(mid)+1):
        n=mid/i
        if mid%n==0:
            if mid%i==0:
                if factorOperation(n,i)==11 or factorOperation(n,i)==12 or factorOperation(n,i)==21 or factorOperation(n,i)==22 or factorOperation(n,i)==31 or factorOperation(n,i)==32 or factorOperation(n,i)==41 or factorOperation(n,i)==42:
                    #print(n,i)
                    z.append(n)
                    z.append(i)
                    break

#check the series of operation used
def factorOperation(p,q):
    global b
    global fac1
    global fac2
    if signCheck()==1:
        if (-p-q)==b:
            fac1=-p
            fac2=-q
            return 11
        elif (-q-p)==b:
            fac1=-q
            fac2=-p
            return 12
    elif signCheck()==2:
        if (-p+q)==b:
            fac1=-p
            fac2=q
            return 21
        elif (-q+p)==b:
            fac1=-q
            fac2=p
            return 22
    elif signCheck()==3:
        if (p+q)==b:
            fac1=p
            fac2=q
            return 31
        elif (q+p)==b:
            fac1=q
            fac2=p
            return 32
    elif signCheck()==4:
        if (p-q)==b:
            fac1=p
            fac2=-q
            return 41
        elif (q-p)==b:
            fac1=q
            fac2=-p
            return 42
        
#Create last equation
def factorOperating():
    global eq
    global fac1,fac2,a,c
    eq.append(a)
    eq.append(fac1)
    eq.append(fac2)
    eq.append(c)
    
#Alg. to take common--incomplete
"""def takingCommon():
    global eq
    global ans
    for i in range(abs(int(eq[0])),0,-1):
        if eq[0]%i==0 and eq[1]%i==0:
            ans.append(i)
    for j in range(abs(int(eq[1])),0,-1):
        if eq[2]%j==0 and eq[3]%j==0:
            ans.append(j)""" 



factorize()
factorCheck()
factorOperating()  
"""takingCommon()""" 
print(y)
print(z)
print(eq)
print(ans)