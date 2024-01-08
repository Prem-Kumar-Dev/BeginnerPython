"""name = input("Write your name:_")
age=int(input("your age:_"))
mark=float(input("your percentage in class 12th:_"))
email=input(("your email:_"))
print("Hello Audiance!\nI am {}. I am {} years old. I have secured {} mark in 12th class. My mail Id is {}.\n Have a nice day ".format(name,age,mark,email))
"""

"""a=float(input("First number:_"))
b=float(input("Second number:_"))
print("Sum:_",a+b)
print("Diff:_",a-b)
print("Product:_",a*b)
print("Divide:_",a/b)
print("Reminder:_",a%b)
print("Dif:_",a//b)
print("Exp:_",a**b)"""

"""a=float(input("Principal:_"))
b=float(input("Rate:_"))
c=float(input("Time:_"))

print("Simple Intrest: ",(a*b*c)/100)
print("Compound Intrest: ",((((b/100)+1)**c)*a)-a)"""
# Km into miles
"""a=float(input("Kilometer:_"))
print("Miles",(a*0.62137))"""

#converting celcius in F
"""a=float(input("Celcius:_"))
print("Ferignheight:_",(a*(9/5)+32))"""

#Swap two number
"""a=float(input("First no:_"))
b=float(input("Second no:_"))
a=a+b
b=a-b
a=a-b
print(a,b)"""

#Square root of a num
"""a=float(input("Number:_"))
print("Square root:_",a**(1/2))"""

#Perimeter
"""a=int(input("1)Perimeter \n 2)Area \n 3)Volume\n Enter your choice:_"))
if a==1:
    a=int(input("1)Rectangel \n 2)Square \n 3)Circle \n 4)Rhombus \n 5)Triangle \n 6)Parallelogram \n Enter your choice:_"))
    if a ==1 or a==6:
        l=float(input("Length:_"))
        b=float(input("Breadth"))
        print("Perimeter:_",(2*(l+b)))
    elif a==2 or a==4:
        s=float(input("Side:_"))
        print("Perimeter:_",(4*s))
    elif a==3:
        r=float(input("Radius:_"))
        print("Perimeter:_",(2*(22/7)*r))
    elif a==5:
        s1=float(input("First Side:_"))
        s2=float(input("Second Side:_"))
        s3=float(input("Third Side:_"))
        print("Perimeter:_",(s1+s2+s3))"""

#Largest Number
"""import array as a

a=a.array('d',[])

while True:
    num=(input("Number OR 'E' for Exit:_"))
    if num=="E"or num=="e":
        break
    a.append(float(num))
    print(a)

b=a[0]
for i in a[1:]:
    if b<i:
        b=i

print(b)"""

#Roots
"""print("Enter the value of x\u00b2:_",end="")
a=float(input())
b=float(input("Enter the coefficient x:_"))
c=float(input("enter the constant:_"))
print("Value of x is {} or {}".format(((-b+((b**2)-4*a*c)**(1/2))/(2*a)), ((-b-((b**2)-4*a*c)**(1/2))/(2*a))))"""


#Operators:
#Boolean
"""print(5>6)
x=int(input(">"))
y=int(input(">"))
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x<=y)
print(x>=y)"""

#Conditionl Statement
"""x=int(input("Number:_"))

if x>0:
    print("{} is Positive".format(x))
elif x==0:
    print("{} is Zero".format(x))
else:
    print("{} is Negative".format(x))"""
#leap year
"""a=int(input("Year:_"))
if a%400==0 and a%100==0:
    print("{} is Leap Year".format(a))
elif a%4==0 and a%100!=0:
    print("{} is Leap Year".format(a))
else:
    print("{} is Not a Leap Year".format(a))"""
#CountDown
"""a=int(input("A Number:_"))
i=0
while i<=a:
    print(a)
    a=a-1"""


#reverse int:
"""a=int(input("The Integer:_"))
num=0
while a!=0:
    d=a%10
    num=(num*10)+d
    a=a//10
print(num)"""


#series
"""a=int(input("Digit:_"))
n=int(input("n:_"))
no=0
sum=0
for i in range(0,n):
    for j in range(i,n):
        no=(no*10)+a
    sum=sum+no
    no=0
print(sum)"""



#fibonachi
"""a=1
b=0
c=int(input("No. of fibonachi:_"))
for i in range(1,c+1):
    print(b,end=" ")
    a,b=b,a+b"""

"""#Pattern
a=10
for i in range(0,a):
    for k in range(i,a-1):
        print(" ",end="")

    for j in range(0,i+1):
        print("* ",end="")
    
    print()"""


"""a="Ram"
b="Mohan"
c=a.swapcase()+b.swapcase()
d=list(c)
print(c)
for i in range(1,len(c)+1,2):
    d[i]=d[i].lower()
c=''.join(d)
print(c)"""

"""def prime(x):
    c=0
    for i in range(2,x+1):
        if x%i==0:
            c+=1
        if c>1:
            print("{} is not a prime number.".format(x))
            break
    if c<=1:
        print("{} is a prime number.".format(x))

prime(11)"""

"""def unique(x):
    a=set(x)
    a=sorted(list(a))
    print(a)

unique([1,6,9,2,6,2,2,6,10])"""


def pasclesNumber(x):
    


