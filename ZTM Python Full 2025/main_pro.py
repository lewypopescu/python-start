# conditional logic & #indentation

# if, elif, else
# if condition:
#     do something
# elif condition:
#     do something
# else:
#     do something

is_good = True
is_awesome = True

if is_good:
    print('You are good!')
elif is_awesome:
    print('You are awesome!')
else:
    print('You are neither good nor awesome!')
print('Always print me!')  # This will always print
if is_good and is_awesome:
    print('You are awesome and good!')
elif is_good or is_awesome:
    print('You are good or awesome!')
else:
    print('You are neither good nor awesome!')
print('Always print me!')  # This will always print

# Nested if statements
if is_good:
    print('You are good!')
    if is_awesome:
        print('You are awesome!')
    else:
        print('You are not awesome!')

# Ternary operator
print('You are awesome!' if is_awesome else 'You are not awesome!')

# Short-circuit evaluation !!!
print('You are awesome and good!' if is_awesome and is_good else 'You are neither good nor awesome!')

# Using the ternary operator with multiple conditions
# print('You are awesome!' if is_awesome else 'You are not awesome!') if is_good else print('You are neither good nor awesome!')

# truthy vs falsy !!!

# 0, '', [], {}, None are falsy
# everything else is truthy
# truthy
print(bool(1))  # True
print(bool('True'))  # True
print(bool('False'))  # True
# falsy
print(bool(0))  # False
print(bool(''))  # False
print(bool([]))  # False
print(bool({}))  # False
print(bool(None))  # False
# truthy vs falsy with lists
print(bool([1, 2, 3]))  # True
print(bool(['']))  # True
print(bool([0]))  # True
print(bool([None]))  # True
print(bool([False]))  # True
print(bool([True]))  # True
print(bool([0, 1, 2]))  # True
print(bool([None, 0, '']))  # True

# logical operators
# and, or, not
# and
print("a" < "b" and 1 < 2)  # True
print("a" < "A")  # False
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
# or
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

print(5 < 10 and 10 > 5)  # True
print(5 < 10 or 10 > 5)  # True

# not
print(not True)  # False
print(not False)  # True
print(not (5 < 10))  # False
print(not (5 > 10))  # True

# is vs ==
# is checks if two variables point to the same object
# == checks if two variables have the same value
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False
print(a == b)  # True
# is not
print(a is not b)  # True
print(a != b)  # False
# in
print(1 in a)  # True
print(4 in a)  # False
print(1 not in a)  # False
print(True is True)  # True
print(False is False)  # True
print("1" is "1")  # True
print([1, 2, 3] is [1, 2, 3])  # False
print(10 is 10)  # True
print([] is [])  # False

# for loops
for i in range(10):
    print(i)

for item in (1, 2, 3, 4, 5):
    for x in ["a", "b", "c"]:
        print(item, x)

for item in "hello world":
    print(item)

# iterables
# iterable - list, dictionary, set, tuple, string
# iterate - to go through each item in an iterable, operate on each item, one by one
user = {
    "name": "John",
    "age": 30,
    "is_good": True
}

for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# range
# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)
for i in range(10, 0, -1):
    print(i)
for i in range(3):
    print(list(range(9)))

# enumerate
# enumerate(iterable, start=0)
# enumerate - to get the index and value of each item in an iterable
for i, char in enumerate("hello world"):
    print(i, char)
for i, char in enumerate("hello world", start=3):
    print(i, char)
for i, item in enumerate(list(range(30))):
    if item == 20:
        print(f"index of 20 is {i}")

# while loops
# while loops - to repeat a block of code while a condition is true
while True:
    response = input("say something: ")
    if response == "bye":
        print("goodbyeee...")
        break
    elif response == "hi":
        print("hellooo")
    else:
        print("Say hi to be on or bye to be off")
        continue

# break, continue, pass
# break - to exit a loop
# continue - to skip the current iteration and move to the next iteration
# pass - to do nothing, just a placeholder, to avoid syntax errors, maybe something will be added later

# functions
# functions - to group a block of code that can be reused

# positional arguments - to pass values to a function in the order they are defined !!


def greet_user(name, age):
    print(f"hello {name},  you are {age} years old")


greet_user("John", 30)
greet_user("Lewy", 26)

# function with keyword arguments
greet_user(age=33, name="Lewy")

# function with default arguments


def greet_user_second(name="Lewy", age=32):
    print(f"hello {name},  you are {age} years old")


greet_user_second()
greet_user_second("John", 34)

# return statement


def add_numbers(a, b, c=0, d=0):
    return a + b + c + d


def sum_one(num1, num2):
    def another_function(n1, n2):
        return n1 + n2
    return another_function(num1, num2)


total = sum_one(10, 20)
print(total)

# methods vs functions
# methods - functions that are defined inside a class
# functions - functions that are defined outside a class
# methods - to call a function on an object
# functions - to call a function without an object
# methods - to operate on an object
# functions - to operate on data
# methods - to operate on a class
# functions - to operate on a module
# methods - to operate on a package
# functions - to operate on a program
# methods - to operate on a script
# functions - to operate on a file
# methods - to operate on a directory
# functions - to operate on a path
big_hello = "hello world".upper()
joined = "hello world".join("999")
print(big_hello)
print(joined)

# docstrings
# docstrings - to document a function, to explain what it does


def greet_user_hello(name):
    """
    This function greets the user
    :param name: name of the user
    :return: None
    """
    print(f"Hello {name}")


greet_user_hello("Lewy")

# help - to get help on a function, to see the docstring
# help(greet_user_hello)
print(greet_user_hello.__doc__)

# function annotations


def add_numbers_hello(a: int, b: int) -> int:
    """
    This function adds two numbers
    :param a: first number
    :param b: second number
    :return: sum of a and b
    """
    return a + b


print(add_numbers_hello(10, 20))

# lambda functions
# lambda functions - to create a small anonymous function
# lambda - to create a function without a name


def add(x, y): return x + y


print(add(2, 3))


# clean code
# clean code - to write code that is easy to read and understand
# clean code - to write code that is easy to maintain and modify
# clean code - to write code that is easy to test and debug
# clean code - to write code that is easy to reuse and share
# clean code - to write code that is easy to document and explain
def is_even(n):
    return n % 2 == 0


print(is_even(10))

# args and kwargs
# args - to pass a variable number of arguments to a function


def add_numbers_args(*args, **kwargs):
    total = 0
    for num in args:
        total += num
    return total + sum(kwargs.values())


print(add_numbers_args(1, 2, 3, 4, 5, a=99, b=20, c=30))

# walrus operator
# walrus operator - to assign a value to a variable and return the value at the same time
a = 10
b = 50
if (c := a + b) > 20:
    print(c)

# scope
# scope - to define the accessibility of a variable, to define the lifetime of a variable
# scope - who have access to who
# 1 - start with local scope
# 2 - Parent scope
# 3 - Global scope
# 4 - Built-in scope
# global keyword - to declare a variable as global, to access a global variable inside a function
x = 10


def my_function_global():
    global x
    y = 20
    print(x, y)


my_function_global()

# local keyword - to declare a variable as local, to access a local variable inside a function
# nonlocal keyword - to declare a variable as nonlocal, to access a nonlocal variable inside a nested function


def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x = 90
        print(x)
    inner_function()
    print(x)


outer_function()

# why do we need scope?
# 1 - to avoid naming conflicts
# 2 - to avoid accidental changes to variables
# 3 - to avoid memory leaks !!!
# 4 - to avoid unexpected behavior
# 5 - to avoid bugs
# 6 - to avoid confusion
# 7 - to avoid complexity
# 8 - to avoid performance issues
# 9 - to avoid security issues
# 10 - to avoid readability issues

# First Python Test - 88% Yeyyy, Good Job Lewy ;) 07/05/2025
