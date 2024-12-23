# Basic Python
# Print a message to the console
print("Hello, World!")

# Assign values to variables
x = 10
y = 5

# Perform addition
result = x + y

# Prompt user for input
name = input("Enter your name: ")

# Conditional statements
if x > y:
    pass  # Executes if x is greater than y
elif x == y:
    pass  # Executes if x equals y
else:
    pass  # Executes if x is less than y

# For loop
for i in range(10):
    pass  # Loops through numbers 0 to 9

# While loop
while x > 0:
    x -= 1  # Decrements x until it reaches 0

# Define a function
def my_function():
    return result  # Returns the value of result

# Importing modules
import math
import os
import sys
import random
from datetime import datetime

# Exception handling
try:
    pass  # Code that might raise an exception
except ValueError as e:
    pass  # Handles ValueError exceptions
finally:
    pass  # Executes cleanup code

# File operations
with open("file.txt", "r") as file:
    data = file.read()  # Reads the content of the file

# Built-in functions
len(data)  # Returns the length of data
type(x)  # Returns the type of x
isinstance(x, int)  # Checks if x is an integer
del x  # Deletes the variable x

# Data structures
list_var = [1, 2, 3, 4, 5]  # List - You can modify, append, remove, and access elements using indices
tuple_var = (1, 2, 3)  # Tuple - Once created, the elements in a tuple cannot be changed.
set_var = {1, 2, 3}  # Set - Sets automatically remove duplicate values.
dict_var = {"key1": "value1", "key2": "value2"}  # Dictionary

# List operations
list_var.append(6)  # Adds 6 to the list 
list_var.remove(3)  # Removes the value 3 from the list
list_var.sort()  # Sorts the list in ascending order
list_var.reverse()  # Reverses the list
max(list_var)  # Returns the maximum value
min(list_var)  # Returns the minimum value
sum(list_var)  # Returns the sum of all elements
list_var[0:3]  # Slices the list from index 0 to 2
list_var[-1]  # Accesses the last element
list_var.index(4)  # Finds the index of value 4

# Dictionary operations
for key, value in dict_var.items():
    pass  # Iterates through dictionary key-value pairs
dict_var["key3"] = "value3"  # Adds a new key-value pair
dict_var.get("key1")  # Retrieves the value for key1
dict_var.pop("key1")  # Removes the key-value pair for key1

# String operations
"Hello".upper()  # Converts to uppercase
"Hello".lower()  # Converts to lowercase
"Hello".startswith("He")  # Checks if the string starts with "He"
"Hello".endswith("lo")  # Checks if the string ends with "lo"
"Hello".replace("e", "a")  # Replaces 'e' with 'a'
"Hello".split("l")  # Splits the string at 'l'
".".join(["a", "b", "c"])  # Joins elements with a period

# Intermediate Python
# Define a class
class MyClass:
    def __init__(self, param):
        self.param = param  # Initializes an instance variable
    def __str__(self):
        pass  # Returns a string representation
    def __repr__(self):
        pass  # Returns a detailed string representation
    @staticmethod
    def static_method():
        pass  # Defines a static method
    @classmethod
    def class_method(cls):
        pass  # Defines a class method

# Lambda function
lambda_func = lambda x: x * 2  # Anonymous function to double a value

# Map, filter, and reduce
list(map(lambda x: x * 2, [1, 2, 3]))  # Applies a function to each list element
list(filter(lambda x: x > 2, [1, 2, 3]))  # Filters elements greater than 2
from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3])  # Reduces a list by summing elements

# List comprehensions
[x for x in range(10)]  # Creates a list of numbers 0 to 9
[x**2 for x in range(10) if x % 2 == 0]  # Squares even numbers

# Utility functions
zip([1, 2, 3], ['a', 'b', 'c'])  # Pairs elements from two lists
enumerate(['a', 'b', 'c'])  # Adds index to elements
list(zip(*zip([1, 2], ['a', 'b'])))  # Unzips a zipped object
all([True, False, True])  # Checks if all elements are True
any([True, False, True])  # Checks if any element is True
sorted([3, 1, 2])  # Sorts in ascending order
sorted([3, 1, 2], reverse=True)  # Sorts in descending order
sorted(dict_var, key=lambda k: dict_var[k])  # Sorts dictionary by values
reversed(list_var)  # Reverses a list

# Set operations
set_var.union({4, 5})  # Combines sets
set_var.intersection({3, 4})  # Finds common elements
set_var.difference({2})  # Finds unique elements

# OS and datetime modules
os.getcwd()  # Gets the current working directory
os.path.exists("file.txt")  # Checks if a file exists
os.remove("file.txt")  # Deletes a file
datetime.now()  # Gets the current date and time

# Random module
random.randint(1, 100)  # Generates a random integer
random.choice(list_var)  # Selects a random element
random.shuffle(list_var)  # Shuffles the list

# Math module
math.sqrt(16)  # Calculates the square root
math.pow(2, 3)  # Raises 2 to the power of 3
math.pi  # Returns the value of pi

# Generator function
def generator_func():
    yield x  # Generates values one at a time

# Advanced Python
# JSON operations
import json
json_data = json.dumps(dict_var)  # Converts a dictionary to JSON
parsed_data = json.loads(json_data)  # Parses JSON back to dictionary

# HTTP requests
import requests
response = requests.get("https://example.com")  # Sends a GET request
response.json()  # Parses JSON response

# Assertions
assert x == 10  # Asserts that x equals 10

# Regular expressions
import re
re.match(r"\d+", "123abc")  # Matches digits at the start of a string

# Exit the program
exit()  # Exits the Python interpreter
