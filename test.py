def calculate_list():
    user_input = input("Enter Number By Spaces")
    add = [int(x) for x in user_input.split()]
    return sum(add)

print(calculate_list())
