"""def findReciprocal(x):
    try:
        x=int(x)
        print("Value:",(1/x))
    except ValueError:
        print("Value Error")
    except ZeroDivisionError:
        print("Cant Divide by zero")
    except:
        print("Handling all Errors")    
findReciprocal("hello")
"""
"""a=int(input("No:"))
try:
    if a<=0:
        print("Value is negative.")
    print("We entered",a)
except ValueError as ve:
    print(a)"""


try:
    f=open("test.txt",encoding='utf-8')
finally:
    f.close()
