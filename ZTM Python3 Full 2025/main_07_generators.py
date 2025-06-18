# Generators
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
