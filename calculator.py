def add():
    from functools import reduce
    f = input("Enter the numbers to add:\n")
    lst = f.split("+")
    print('the sum of {} is equals to {}'.format(
        lst, reduce(lambda a, b: float(a)+float(b), lst)))


def subtract():
    from functools import reduce
    f = input("Enter the numbers to subtract:\n")
    lst = f.split("-")
    print('the subtraction of {} is equals to {}'.format(
        lst, reduce(lambda a, b: float(a)-float(b), lst)))


def multiply():
    from functools import reduce
    f = input("Enter the numbers to multiply:\n")
    lst = f.split("*")
    print('the product of {} is equals to {}'.format(
        lst, reduce(lambda a, b: float(a)*float(b), lst)))


def divide():
    from functools import reduce
    f = input("Enter the numbers to divide:\n")
    lst = f.split("/")
    try:
        print('the division of {} is equals to {}'.format(
            lst, reduce(lambda a, b: float(a)/float(b), lst)))
    except ZeroDivisionError:
        print("Can't divide by zero: Undefined")


def lcm():
    import LCM


def hcf():
    import HCF


def martix_multiply():
    from matrix import multiply
    multiply()
