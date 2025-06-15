class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items."""

    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."

# Sample Product Inventory
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0,  # Out of stock
    "grapes": 3
}

def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")

# Testing the Custom Exception
try:
    purchase_item("apple", 3)  # Purchase successful
    purchase_item("orange", 1)  # Raises OutOfStockError
    purchase_item("watermelon", 1)  # Item not available
except OutOfStockError as e:
    print(e)  # Output:
    
    
# Exercise 1: Handling ZeroDivisionError

# Instructions:

# Write a program that takes two numbers as input from the user and divides the first number by the second number.
# Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
    
# Exercise 2: File Handling with FileNotFoundError

# Instructions:

# Write a program that attempts to open and read data from a file specified by the user.
# Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.

try:
    fileName = input("Enter the filename to open: ")
    
    with open(fileName, 'r') as file:
        content = file.read()
        print("\n file content")
        print(content)
        
except FileNotFoundError:
    print(f" Error: The file '{fileName}' was not found. Please check the name and try again.")
    
# Exercise 3: Custom Exception

# Instructions:

# Create a custom exception class called ValueTooHighError that inherits from the Exception class.
# Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.

class ValueTooHighError(Exception):
    def __init__(self, number):
        self.number = number
    
    def __str__(self):
        return f"the number {self.number} is greater than 100"
try:
    num = int(input(f"Enter the number: "))
    if num > 100:
        raise ValueTooHighError(num)
    else:
        print(num)
except ValueTooHighError as e:
    print(e)