# Run with python datatypes.py
# Datatypes 
text = "Hello World"
number = 42
pi = 3.14
is_valid = True
print(type(text))  # Output: <class 'str'>
print(type(number))  # Output: <class 'int'>
print(type(pi))  # Output: <class 'float'>
print(type(is_valid))  # Output: <class 'bool'>

# A tuple is an ordered, immutable collection of elements, defined using parentheses (). 
tuple_example = (1, 2, 3, 4)
print(type(tuple_example))  # Output: <class 'tuple'>
print(tuple_example[0])  # Output: 1
print(tuple_example[3])  # Output: 4

# A list is an ordered, mutable collection of elements, defined using square brackets [].
list_example = [1, 2, 3]
print(type(list_example))  # Output: <class 'list'>
print(list_example[0])  # Output: 1
print(list_example[2])  # Output: 3

names_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
print(names_list[0])  # Output: Alice
print(names_list[5])  # Output: Frank

# A dictionary is an unordered collection of key-value pairs, defined using curly braces {}.
person_dict = {"name": "Alice", "age": 30, "city": "New York", "occupation": "Engineer", "hobbies": ["reading", "traveling", "cooking"], "is_student": False}
print(type(person_dict))  # Output: <class 'dict'>
print(person_dict["name"])  # Output: Alice
print(person_dict["city"])  # Output: New York
print(person_dict["occupation"])  # Output: Engineer
print(person_dict["hobbies"])  # Output: ['reading', 'traveling', 'cooking']
print(person_dict["is_student"])  # Output: False

# It is a collection of unique elements, defined using curly braces {}. 
# Sets are unordered and do not allow duplicate values.
unique = {8,7, 1, 2, 3, 4, 4, 5}
print(type(unique))  # Output: <class 'set'>
print(unique)  # Output: {1, 2, 3, 4, 5, 7, 8}