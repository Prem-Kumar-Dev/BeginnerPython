def febo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return febo(n-1)+febo(n-2)

i=int(input("The no of fibonachi:_"))
for n in range(0,i):

    print(febo(n))
    