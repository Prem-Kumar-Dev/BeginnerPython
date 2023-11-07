def smallest(x):
    c=0
    for x in a:
        x=int(x)
        if c==0:
            b=x
            c=c+1
        elif b>x:
            b=x
    return b
def largest(x):
    b=0
    for x in a:
        x=int(x)
        if b<x:
            b=x
    return b
def prime(x):
    prime=x
    c=0
    if prime==2:
        return prime
    for i in range(2,prime):
        if prime%i==0:
            c=c+1
        if c>0:
            break
        if c==0:
            return prime




def pr(x):
    global a
    l=largest(a)
    while True:
        p=l
        
        count=0
        for n in a:
            if p%int(n)==x:
                count=count+1
        if count==len(a)-1:
            return p
        l=l+1
        





a=input().split()

s=smallest(a)
print(pr(s))






