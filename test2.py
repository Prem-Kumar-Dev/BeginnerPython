a=10
for i in range(0,a):
    for k in range(i,a-1):
        print(" ",end="")

    for j in range(0,i+1):
        print("* ",end="")
    
    print()

for i in range (a-1,0,-1):
    for k in range(i,a):
        print(" ",end="")
    
    for j in range(i,0,-1):
        print("* ",end="")
    print()

