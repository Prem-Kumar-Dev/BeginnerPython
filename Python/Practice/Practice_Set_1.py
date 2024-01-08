def PS1No1():
    #1) Addition of two numbers:
    a=float(input("1st Number:_"))
    b=float(input("2nd Number:_"))
    print("{} + {} = {}".format(a,b,a+b))

def PS1No2():
    #2) Average of three number:
    a=float(input("1st Number:_"))
    b=float(input("2nd Number:_"))
    c=float(input("3rd Number:_"))
    print("Average of {},{},{} = {}".format(a,b,c,(a+b+c)/3))

def PS1No3():
    #3) Sum of 5 subject and its percentage:
    a=float(input("Mark in 1st Subject(out of 100):_"))
    b=float(input("Mark in 2nd Subject(out of 100):_"))
    c=float(input("Mark in 3rd Subject(out of 100):_"))
    d=float(input("Mark in 4th Subject(out of 100):_"))
    e=float(input("Mark in 5th Subject(out of 100):_"))
    print("Total mark = {} and Percentage = {}%".format(a+b+c+d+e,((a+b+c+d+e)/500)*100))

def PS1No4():
    #4) Area of a circle:
    r=float(input("Radius:_"))
    print("Area = {} sq. units".format((22/7)*r**2))

def PS1No5():
    #5) Area of a Rectangle:
    l=float(input("Length:_"))
    b=float(input("Breadth:_"))
    print("Area = {} sq. units".format(l*b))

def PS1No6():
    #6) Fahrenheit in to Celsius:
    t=float(input("Temp.(in F):_"))
    print("{} F = {} C".format(t,(t-32)*(5/9)))

def PS1No7():
    #7) Swap values of two Varible:
    a=float(input("First no:_"))
    b=float(input("Second no:_"))
    a=a+b
    b=a-b
    a=a-b
    print(a,b)

def PS1No8():
    #8) Calculate age of Shreya:
    ref_year=2001; ref_age=10
    given_year=2021; age_2021= (given_year-ref_year)+ref_age
    print("Age of Shreya in 2021 is:",age_2021)

def PS1No9():
    #9) a)Multiply two numbers: b) print age in months:
    a=float(input("1st Number:_"))
    b=float(input("2nd Number:_"))
    print("{} * {} = {}".format(a,b,a*b))

    age=int(input("Age(in years):_"))
    print("Your age in months is", age*12)



PS1No1()
PS1No2()

