# Functional Programming
# Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data.
# It emphasizes the use of functions as first-class citizens, meaning functions can be passed as arguments, returned from other functions, and assigned to variables.
# Functional programming promotes immutability, higher-order functions, and pure functions.
# It encourages a declarative programming style, focusing on what to solve rather than how to solve it.
# Functional programming is often contrasted with imperative programming, which focuses on changing state and executing sequences of commands.
# In Python, functional programming features include:
# - First-class functions: Functions can be assigned to variables, passed as arguments, and returned from other functions.
# - Higher-order functions: Functions that take other functions as arguments or return them as results.
# - Lambda functions: Anonymous functions defined using the `lambda` keyword.
# - Map, filter, and reduce: Functions for applying operations to collections.

# Pure functions: Functions that always produce the same output for the same input and have no side effects.
# - Immutability: Emphasizing the use of immutable data structures.
def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat


def multiply_by_two(list):
    new_list = []
    for item in list:
        new_list.append(item * 2)
    return new_list


my_list = [1, 2, 3, 4, 5, 6]

print(list(multiply_by_two(my_list)))
print(my_list)

# map - applies a function to each item in an iterable and returns a map object (which can be converted to a list)


def multiply_by_two_map(item):
    return item * 2


print(list(map(multiply_by_two_map, my_list)))
print(my_list)

# filter - filters elements based on a condition


def is_even(item):
    return item % 2 == 0


print(list(filter(is_even, my_list)))
print(my_list)

# zip - combines elements from multiple lists into tuples
second_list = [10, 20, 30, 40, 50, 60]
third_list = [100, 200, 300, 400, 500, 600]

print(list(zip(my_list, second_list, third_list)))
print(my_list)
print(second_list)
print(third_list)
