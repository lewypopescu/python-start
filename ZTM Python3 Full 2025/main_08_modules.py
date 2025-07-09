# Modules - importing and using modules

import main_08_test_modules

# from main_08_test_modules import * # Importing all functions from the module

from main_08_test_package import shopping_cart

import random
# import random as lalala # Importing the random module with an alias

import sys  # Importing the sys module to access system-specific parameters and functions

import pyjokes

from collections import Counter, defaultdict

import datetime

from array import array

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(Counter(li))  # Counts the occurrences of each element in the list

print(main_08_test_modules.add(3, 9))

print(main_08_test_modules.subtract(9, 6))

print(main_08_test_modules.multiply(3, 3))

print(main_08_test_modules.divide(9, 3))

# Using the ShoppingCart class from the shopping_cart module
shopping_cart_one = shopping_cart.ShoppingCart()

if __name__ == '__main__':
    print('This module is being run directly. Main module name:', __name__)
    print(shopping_cart_one.add('wine'))
    print(shopping_cart_one.add('wine'))
    print(shopping_cart_one.add('water'))
    print(shopping_cart_one.add('candy'))
    print(shopping_cart_one.add('chips'))
    print(shopping_cart_one.remove('chips'))

print(__name__)

print(random)  # This will print the module object, not the random number itself
# print(help(random))  # Displays help information about the random module
print(random.random())  # Generates a random float between 0.0 and 1.0
print(random.randint(0, 99))  # Generates a random integer between 1 and 100
# Randomly selects an item from the list, tastyyy ;)
print(random.choice(['wine', 'water', 'redbull']))

a_list = [1, 2, 3, 4, 5]
random.shuffle(a_list)  # Shuffles the list in place
print(a_list)

# This is a list that contains the command-line arguments passed to the script, where sys.argv[0] is the script name and subsequent elements are the arguments passed.
sys.argv

first_argument = sys.argv[1] if len(sys.argv) > 1 else None
print(f"First command-line argument: {first_argument}")

# Environment variables can be accessed using sys module
# sys.path is a list of directories that Python searches for modules when importing
# sys.path.append('/path/to/directory')  # You can add a directory to the module search path
# Python modules are files containing Python code that can define functions, classes, and variables.
# They allow you to organize your code into reusable components.
# Python packages are a way of organizing related modules into a directory hierarchy.
# A package is a directory that contains a special __init__.py file (which can be empty) and one or more module files.
# Modules can be imported using the import statement, and you can access their functions and classes using the dot notation.

# Virtual environments can be created using the venv module
# venv is a module that allows you to create isolated Python environments - for example, you can create a virtual environment for a project to manage dependencies separately from the global Python installation.

joke = pyjokes.get_joke("en", category="neutral")
print(f"Here's a joke for you: {joke}")

li = [1, 2, 2, 4, 4, 6, 6, 9, 9, 9]
print(Counter(li))  # Counts the occurrences of each element in the list

sentence = "This is a test sentence for counting words. yeyy"
# Counts the occurrences of each character in the sentence
print(Counter(sentence))
word_count = Counter(sentence.split())
# Counts the occurrences of each word in the sentence
print(f"Word count: {word_count}")

dictionary = defaultdict((lambda: 3), {"a": 1, "b": 2, "c": 4})
print(dictionary["a"])  # Outputs 1
# Outputs 3, since "d" is not in the dictionary, it returns the default value (3)
print(dictionary["d"])
# Ordered dictionary maintains the order of insertion, but they are not as commonly used in Python 3.7 and later, where regular dictionaries maintain insertion order.

print(datetime.datetime.now())  # Prints the current date and time

# Demonstrating the use of array module
arr = array('i', [1, 2, 3, 4, 5])  # 'i' indicates an array of integers
print(arr)  # Prints the array
print(arr[2])  # Accessing the first element of the array
