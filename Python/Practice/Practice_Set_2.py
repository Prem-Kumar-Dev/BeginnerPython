def PS2No1():
    #1) Print function:

    print("Hello, Python!")
    print('Hello, Python!')
    # print(Hello, Python!) ---> SyntaxError: invalid syntax
    # print 'Hello, Python!'---> SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
    # print('Hello, Python!') print('Hello, Python!') print('Hello, Python!')  ---> SyntaxError: invalid syntax
    print('Hello, Python!')
    print('Hello, Python!')
    print('Hello, Python!')

def PS2No2():
    #2) Use of \n and \"...\":
    print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")

def PS2No3():
    #3) Type of Data:
    print(type(6))
    print(type("Welcome"))
    print(type(True))
    print(type(8.0))

def PS2No4():
    #4) Length of Hypotenuse:
    p=float(input("Length of the Perpendicular side:_"))
    b=float(input("Length of the Base:_"))
    print("Lenght of Hypotenus whose Base={} & Perpendicular={} is {} ".format(b,p,(((b**2)+(p**2))**(1/2))))

def PS2No5():
    #5) Calculation:
    print(8.0//5+4*9%(3+1)/6-1**2**3)

def PS2No6():
    print("Programming","Essentials","in",sep="***",end="...")
    print("Python")

def PS2No7():
    radius=float(input("Radius:_"))
    area=(3.14*radius*radius)
    print("Area = {} sq. units".format(area))

def PS2No8():
    # Miles to Kilometers:
    miles=float(input("The distance(in miles:_)"))
    print("{} miles = {} kilometers".format(miles,miles*1.61))

    # Kilometers to Miles:
    kilometers=float(input("The distance(in kilometers:_)"))
    print("{} kilometers = {} miles".format(kilometers,kilometers/1.61))

def PS2No9():
    a=("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n")
    print(a*2)
    b=("    *         *\n   * *       * *\n  *   *     *   *\n *     *   *     *\n***   *** ***   ***\n  *   *     *   *\n  *   *     *   *\n  *****     *****\n")
    print(b)
    

PS2No6()