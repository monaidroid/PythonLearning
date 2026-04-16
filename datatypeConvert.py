# Run with python datatypeConvert.py
# Convert string datatype into number datatype 
# The int() function is used to convert a string to an integer.
# While the float() function is used to convert a string to a floating-point number.
number_str = "42"
number_int = int(number_str)
print(10 + number_int)  # Output: 52
print(type(number_int))  # Output: <class 'int'>  

float_str = "3.14"
print(10.12 +  float(float_str))  # Output: 13.26
print(type(float(float_str)))  # Output: <class 'float'>    

age : int= 30
print(type(age))  # Output: <class 'int'>
name : str = "Alice"
print(type(name))  # Output: <class 'str'>
print("The age of '" + name + "' is " + str(age) + " years.")  # Output: The age of 'Alice' is 30 years.

# Using f-string for better readability and performance
print(f"The age of '{name}' is {age} years.")  # Output: The age of 'Alice' is 30 years.
print(f'Name: {name}, Age: {age}')  # Output: Name: Alice, Age: 30