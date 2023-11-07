a=int(input("No. of lines:_"))
b=input("Symbol:_")
d=input("Border:_")

for i in range(0,a):
    counter=0
    for k in range(i,a-1):
        print(" ",end="")

    for j in range(0,i+1):
        if counter==0 or counter==i:
            print("{} ".format(d),end="")
        else:
            print("{} ".format(b),end="")
        counter+=1
    
    print()

for i in range (a-1,0,-1):
    counter=0
    for k in range(i,a):
        print(" ",end="")
    
    for j in range(i,0,-1):
        if counter==0 or counter==i-1:
            print("{} ".format(d),end="")
        else:
            print("{} ".format(b),end="")
        counter+=1

    print()