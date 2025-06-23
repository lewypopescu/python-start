# Generators
from time import time


def my_generator():
    for i in range(10):
        yield i * 2  # Yielding double the value of i


# Example usage of the generator
gen = my_generator()
print(next(gen))  # Retrieves the first value from the generator
print(next(gen))  # Retrieves the second value from the generator
print("hereeeeeeee")
for value in gen:
    # Iterates through the remaining values in the generator - this will print 4, 6, 8, ..., 18
    print(value)

# iterable - an object that can return its members one at a time, allowing it to be iterated over in a for loop.
# iterator - an object that implements the iterator protocol, which consists of the methods __iter__() and __next__().
# iterate - to go through each item in an iterable, operating on each item one by one.

# Generator - a special type of iterator that is defined using a function with the yield statement.
# yield - a keyword used in a function to make it a generator, allowing it to produce a series of values over time instead of returning a single value.
# Generators are more memory efficient than lists because they generate values on-the-fly and do not store them in memory.


def generator_function(num):
    for i in range(num):
        yield i


for item in generator_function(8):
    print(item)

g = generator_function(3)
# next() - used to retrieve the next item from an iterator or generator.
# next(g) - Returns the next item from the generator
print(next(g))  # Output: 0
print(next(g))  # Output: 1
print(next(g))  # Output: 2
# print(next(g))  # Raises StopIteration exception since there are no more items


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)  # Appending double the value of i to the list
    return result


my_list = make_list(9)
print(my_list)
print(list(range(9)))

# Performance of generators - generators are more memory efficient than lists because they yield values one at a time and do not store the entire sequence in memory. So generators are really, really useful when calculating large sets of data.


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, *kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    print('1')
    for i in range(10000000):  # it finishes faster
        i*5


long_time()
print()


@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):  # it took longer.
        i*5


long_time2()
print()

# Special for loops - using generators in a for loop allows you to iterate over the values produced by the generator without needing to store them all in memory at once.


def special_for(iterable):
    iterator = iter(iterable)  # Converts the iterable into an iterator
    while True:
        try:
            item = next(iterator)  # Retrieves the next item from the iterator
            # print(item * 3)  # Prints the item multiplied by 3
            yield item * 3  # Yields the item multiplied by 3
        except StopIteration:
            break


# This will iterate through the range object without storing all values in memory
test_list = special_for(range(9))
print(list(test_list))


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # this line allows us to use the current number as the starting point for the iteration
        MyGen.current = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(3, 9)
for i in gen:
    print(i)

# go go go go :) > > >
