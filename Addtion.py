def add():
    from functools import reduce
    f = input("Enter the numbers:\n")
    lst = f.split("+")
    print('the sum of {} is equals to {}'.format(
        lst, reduce(lambda a, b: int(a)+int(b), lst)))


def subtract():
    from functools import reduce
    f = input("Enter the numbers:\n")
    lst = f.split("-")
    print('the subtraction of {} is equals to {}'.format(
        lst, reduce(lambda a, b: int(a)-int(b), lst)))


def multiply():
    from functools import reduce
    f = input("Enter the numbers:\n")
    lst = f.split("*")
    print('the product of {} is equals to {}'.format(
        lst, reduce(lambda a, b: int(a)*int(b), lst)))


def divide():
    from functools import reduce
    f = input("Enter the numbers:\n")
    lst = f.split("/")
    try:
        print('the division of {} is equals to {}'.format(
            lst, reduce(lambda a, b: int(a)/int(b), lst)))
    except ZeroDivisionError:
        print("Can't divide by zero: Undefined")


divide()
