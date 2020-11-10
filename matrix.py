from numpy import *

# multiplication of matrics:


def multiply():

    # user input
    lst1 = input("Enter the list 1  (seperated by ',')\n")
    row1 = int(input("Enter the no. of rows:\n"))
    column1 = int(input("Enter the no. of column:\n"))

    lst2 = input("Enter the list 2  (seperated by ',')\n")
    row2 = int(input("Enter the no. of rows:\n"))
    column2 = int(input("Enter the no. of column:\n"))

# converting user input to oragnized data
    lst1 = lst1.split(',')
    arr1 = array(lst1)
    arr1 = arr1.reshape(row1, column1)

    lst2 = lst2.split(',')
    arr2 = array(lst2)
    arr2 = arr2.reshape(row2, column2)

# coordinates x=row y= column
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

# veriable
    calc = 0
    arr = []

# freaking calculation
    for x in range(0, row1):
        x1 = x

        for i in range(0, column2):
            y2 = i

            for n in range(0, column1):
                calc = int(calc)+(int(arr1[x1, y1])*int(arr2[x2, y2]))
                y1 = y1+1
                x2 = x2+1
            arr.append(calc)

# reset veriables
            x1 = x
            x2 = 0
            y1 = 0
            y2 = i
            calc = 0

# output
    arr3 = array(arr)
    arr3 = arr3.reshape(column2, row1)
    print("\nMatrix multiplication of\n\n", arr1,
          "\n\n&\n\n", arr2, "\n\nis equals to\n\n", arr3)


kljl
