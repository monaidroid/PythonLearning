# Run with python functions.py
# functions using 'def' keyword 

# This function takes a name as an argument and returns a greeting message.
def greet(name):
    return f"Hello, {name}!"

# Calling the function with an argument
print(greet("Alice"))  # Output: Hello, Alice!

# This function takes two numbers as arguments and returns their sum.
def add(a, b):
    return a + b
# Calling the function with arguments
print(add(5, 3))  # Output: 8

#  This function takes two numbers with datatype and return with datatype
def multiply(x: float, y: int) -> int :
    return int(x*y) # output will be in integer datatype

# calling function with an argument
print(multiply(x = 3.14, y = 3)) # output : 9

# This function takes a list of numbers and returns their average.
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers) 
# Calling the function with a list of numbers
print(average([10, 20, 30])) # output : 20.0

#This function takes default value as argument and return none
def greet(name:str, greeting:str = 'Hello,') -> None:
    print(f'{greeting} {name}!')

# calling the function with and without default values
greet('Alice') # Output : Hello, Alice! 
greet('Bob', 'Hi') # output : Hi Bob!
greet(name = "Charlie!", greeting = "Welcome") # output : Welcome Charlie!!