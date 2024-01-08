a=str(input("A number:_"))
b=list(a)
n=len(a)
sum=0
for i in b:
    sum=sum+(int(i)**n)

if sum==int(a):
    print("{} is an Armstrong number!".format(a))
else:
    print("{} is not an Armstrong number!".format(a))

