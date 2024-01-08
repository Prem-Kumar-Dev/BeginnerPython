

def sum_of_digits():
    number = input("Enter a number: ")
    total = sum(int(digit) for digit in number)
    print("Sum of digits:", total)

def area_of_circle():
    from math import pi
    radius = float(input("Enter the radius of the circle: "))
    area = pi * (radius ** 2)
    print("Area of the circle:", area)

def best_of_two_averages():
    marks = [float(input(f"Enter marks for test {i+1}: ")) for i in range(3)]
    marks.remove(min(marks))
    average = sum(marks) / 2
    print("Best of two test average marks:", average)

def multiply_by_four_bitwise():
    number = int(input("Enter a number: "))
    result = number << 2
    print("Result after multiplying by 4:", result)

def bitwise_negation():
    a = 15
    print("Bitwise negation of 15:", ~a)

def vowel_or_consonant():
    alphabet = input("Enter an alphabet: ").lower()
    if alphabet in 'aeiou':
        print(alphabet, "is a vowel.")
    else:
        print(alphabet, "is a consonant.")

def largest_of_three():
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(3)]
    print("The largest number is:", max(numbers))

def check_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

def check_characters_equal():
    char1 = input("Enter first character: ")
    char2 = input("Enter second character: ")
    if char1 == char2:
        print("Characters are equal.")
    else:
        print("Characters are not equal.")

def factorial():
    number = int(input("Enter a number: "))
    fact = 1
    if number < 0:
        print("Factorial does not exist for negative numbers.")
    elif number == 0:
        print("The factorial of 0 is 1.")
    else:
        for i in range(1, number + 1):
            fact *= i
        print("The factorial of", number, "is", fact)

def countdown():
    number = int(input("Enter a number for the countdown: "))
    while number >= 0:
        print(number)
        number -= 1

def reverse_integer():
    number = int(input("Enter an integer number: "))
    print("Reversed number:", int(str(number)[::-1]))

def fibonacci_series():
    a, b = 0, 1
    while a <= 50:
        print(a, end=' ')
        a, b = b, a + b

def sum_of_series():
    n = int(input("Enter the number of terms: "))
    total = sum(int("2" * i) for i in range(1, n + 1))
    print("Sum of the series:", total)

def create_and_add_list():
    lst = []
    while True:
        item = input("Enter an item to add to the list (or 'done' to finish): ")
        if item == 'done':
            break
        lst.append(item)
    print("List:", lst)

def reverse_list():
    lst = input("Enter a list of items separated by space: ").split()
    lst.reverse()
    print("Reversed list:", lst)

def add_lists_indexwise():
    L1 = ["M", "NA"]
    L2 = ["Y", "ME"]
    combined = [i + j for i, j in zip(L1, L2)]
    print("Combined list:", combined)

def print_odd_position_elements():
    lst = input("Enter a list of items separated by space: ").split()
    print("Elements at odd positions:", lst[1::2])

def access_string():
    S = input("Enter a string: ")
    print("Accessing string by indexing:", S[0], "and slicing:", S[:])

def replace_vowels():
    S = input("Enter a string: ")
    vowels = 'aeiouAEIOU'
    print("".join('_' if char in vowels else char for char in S))

def split_uppercase():
    sentence = input("Enter a sentence: ")
    words = sentence.upper().split()
    print("Words in uppercase:", words)

def check_palindrome():
    string = input("Enter a string: ")
    if string == string[::-1]:
        print(string, "is a palindrome.")
    else:
        print(string, "is not a palindrome.")

# Additional functions as per the extended request

def create_and_use_tuple():
    my_tuple = ("apple", "banana", "cherry")
    item_to_check = input("Enter an item to check in the tuple: ")
    if item_to_check in my_tuple:
        print(f"{item_to_check} is in the tuple.")
    print("Accessing items:", my_tuple[1])  # Accessing the second item
    # Tuples are immutable, so you can't add items directly. You can concatenate tuples.
    new_item = input("Enter an item to add to the tuple: ")
    my_tuple += (new_item,)
    print("New tuple:", my_tuple)
    print("Length of tuple:", len(my_tuple))

def find_repeated_items_in_tuple():
    my_tuple = (1, 2, 3, 2, 4, 5, 2, 6, 2)
    repeated_items = {i for i in my_tuple if my_tuple.count(i) > 1}
    print("Repeated items:", repeated_items)

def create_and_use_set():
    my_set = {"apple", "banana", "cherry"}
    item_to_check = input("Enter an item to check in the set: ")
    if item_to_check in my_set:
        print(f"{item_to_check} is in the set.")
    # Sets are unordered, so you can't access items using indexes.
    my_set.add(input("Enter an item to add to the set: "))
    print("New set:", my_set)

def display_common_letters():
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    common_letters = set(string1) & set(string2)
    print("Common letters:", common_letters)

def generate_dict_square():
    n = int(input("Enter a number: "))
    square_dict = {i: i * i for i in range(1, n + 1)}
    print("Dictionary with squares:", square_dict)

def dictionary_methods():
    my_dict = {'name': 'John', 'age': 25}
    print("Dictionary items:", my_dict.items())
    print("Access item with key 'name':", my_dict['name'])
    print("Using get() to access 'age':", my_dict.get('age'))
    my_dict['age'] = 26
    print("Changed 'age' to:", my_dict['age'])
    print("Length of dictionary:", len(my_dict))

def sort_dict_and_find_values():
    my_dict = {'a': 3, 'b': 1, 'c': 2}
    sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    min_value = min(sorted_dict_asc.values())
    max_value = max(sorted_dict_asc.values())
    print("Dictionary sorted in ascending order:", sorted_dict_asc)
    print("Dictionary sorted in descending order:", sorted_dict_desc)
    print("Smallest value:", min_value)
    print("Largest value:", max_value)

def file_read_write():
    filename = input("Enter the filename to write and read: ")
    with open(filename, 'w') as file:
        file.write(input("Enter text to write in the file: "))
    with open(filename, 'r') as file:
        print("Content of the file:", file.read())

def check_prime():
    number = int(input("Enter a number: "))
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                print(number, "is not a prime number.")
                break
        else:
            print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

def unique_elements(L):
    return sorted(set(L))

def pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    for row in triangle:
        print(row)

def handle_zero_division():
    try:
        a = float(input("Enter the numerator: "))
        b = float(input("Enter the denominator: "))
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")

def handle_arithmetic_error():
    try:
        a = float(input("Enter the numerator: "))
        b = float(input("Enter the denominator: "))
        result = a / b
        print("Result of division:", result)
    except ArithmeticError:
        print("Arithmetic error occurred during division.")

def add_two_integers():
    try:
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
        print("Sum of the two integers:", a + b)
    except ValueError:
        print("Please enter valid integers.")
    except Exception as e:
        print(f"An error occurred: {e}")

def input_integer():
    try:
        number = int(input("Enter an integer: "))
        print("Valid integer entered:", number)
    except ValueError:
        print("This is not a valid integer. Please try again.")

def handle_keyboard_interrupt():
    try:
        number = input("Enter a number: ")
        print("You entered:", number)
    except KeyboardInterrupt:
        print("\nInput cancelled by the user.")