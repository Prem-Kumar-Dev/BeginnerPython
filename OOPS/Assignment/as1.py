"""class Vehicle:
    def __init__(self,chassis_no, reg_no, max_speed,fuel):
        self.chassis_no = chassis_no
        self.reg_no = reg_no
        self.max_speed = max_speed
        self.fuel = fuel
    
class Car(Vehicle):
    def __init__(self,chassis_no, reg_no, max_speed,fuel,make, model, color, numdoors, transmission, airbags,price):
        super().__init__(chassis_no, reg_no, max_speed,fuel)
        self.make = make
        self.model = model
        self.color = color
        self.numdoors = numdoors
        self.transmission = transmission
        self.airbags = airbags
        self.price = price

class Truck(Vehicle):
    def __init__(self,chassis_no, reg_no, max_speed,fuel,payload,towing,wheelbase,wheels):
        super().__init__(chassis_no, reg_no, max_speed,fuel)
        self.payload = payload
        self.towing = towing
        self.wheelbase = wheelbase
        self.wheels = wheels

class Bike(Vehicle):
    def __init__(self,chassis_no, reg_no, max_speed,fuel,seat_height, wheel_size, engine_size, acc):
        super().__init__(chassis_no, reg_no, max_speed,fuel)
        self.seat_height = seat_height
        self.wheel_size = wheel_size
        self.engine_size = engine_size
        self.acc = acc

c1=Car("991155","KA01",200,50,"Maruti","Swift","Red",4,"Manual",2,500000)
t1=Truck("991156","KA02",100,100,"1000kg","1000kg","1000mm","8")
b1=Bike("991157","KA03",150,30,"800mm","18inch","150cc",10)

print(c1.__dict__)
print(t1.__dict__)
print(b1.__dict__)       """
from datetime import datetime
"""
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()

    def calculate_age(self):
        today = datetime.now().date()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

# Example usage:
person1 = Person("John Doe", "USA", "1990-05-15")
print(f"{person1.name} is {person1.calculate_age()} years old.")"""

"""class Bank:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def display(self):
        return f"Account No: {self.account_no}\nName: {self.name}\nBalance: {self.balance}"
    
class Customer(Bank):
    def __init__(self, account_no, name, balance, withdrawal, deposit):
        super().__init__(account_no, name, balance)
        self.withdrawal = withdrawal
        self.deposit_amount = deposit

    def process(self):
        if self.withdrawal is None:
            self.withdrawal = 0
        if self.deposit_amount is None:
            self.deposit_amount = 0
        
        self.balance = self.balance - self.withdrawal + self.deposit_amount
        return self.display()  # Return updated account details

# Example usage:
customer = Customer("12345", "John Doe", 1000, 200, 500)
print(f"Before processing:\n{customer.display()}\nAfter processing:\n{customer.process()}")"""

"""class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store items and their quantities

    def add_item(self, item_name, quantity, price_per_unit):
        if item_name in self.items:
            self.items[item_name]["quantity"] += quantity
        else:
            self.items[item_name] = {"quantity": quantity, "price_per_unit": price_per_unit}

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if quantity >= self.items[item_name]["quantity"]:
                del self.items[item_name]
            else:
                self.items[item_name]["quantity"] -= quantity

    def calculate_total_price(self):
        total_price = 0
        for item_name, item_info in self.items.items():
            total_price += item_info["quantity"] * item_info["price_per_unit"]
        return total_price

# Example usage:
cart = ShoppingCart()
cart.add_item("Apple", 2, 10)
cart.add_item("Banana", 3, 5)
cart.add_item("Orange", 1, 15)
print(f"Total price: {cart.calculate_total_price()}")
cart.remove_item("Banana", 2)
print(f"Total price after removing 2 bananas: {cart.calculate_total_price()}")"""

class Calculator:
    def __init__(self):
        pass

    def __add__(self, num1, num2):
        return num1 + num2

    def __sub__(self, num1, num2):
        return num1 - num2

    def __mul__(self, num1, num2):
        return num1 * num2

    def __truediv__(self, num1, num2):
        return num1 / num2 if num2 != 0 else "Error: Division by zero!"

    def __floordiv__(self, num1, num2):
        return num1 // num2 if num2 != 0 else "Error: Division by zero!"

    def __mod__(self, num1, num2):
        return num1 % num2 if num2 != 0 else "Error: Division by zero!"

    def __pow__(self, num1, num2):
        return num1 ** num2

# Create an instance of the Calculator class
calculator = Calculator()

# Get user input for numbers and operator
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, //, %, **): ")
num2 = float(input("Enter second number: "))

# Perform operation based on the operator and print result
print(
    "Result:",
    (
        calculator.__add__(num1, num2) if operator == '+' else
        calculator.__sub__(num1, num2) if operator == '-' else
        calculator.__mul__(num1, num2) if operator == '*' else
        calculator.__truediv__(num1, num2) if operator == '/' else
        calculator.__floordiv__(num1, num2) if operator == '//' else
        calculator.__mod__(num1, num2) if operator == '%' else
        calculator.__pow__(num1, num2) if operator == '**' else
        "Invalid operator!"
    )
)



