# Decorators
def hello():
    print("Hello, Worlddd!")


greet = hello
greet()  # Calls the hello function
del hello  # Deletes the original hello function
# print(hello)  # Raises an error because hello is deleted
# This will still work because greet is a reference to the original function:
print(greet())  # Calls the hello function through greet


def hello2(func):
    func()


def greet2():
    print("Hello, Worldd again 222!")

    def func():
        return 9
    return func  # Returns the inner function


a2 = hello2(greet2)  # Calls the greet2 function through hello2
print(a2)  # This will print None because hello2 does not return anything

# Higher Order Function - HOF - a function that takes another function as an argument or returns a function as a result
# filter, map, reduce are examples of higher order functions in Python


def func_hof(func):
    func()


def greet_hof():
    def inner_greet_hof():
        return 9
    print("Hello from the inner function of greet_hof!")
    return inner_greet_hof  # Returns the inner function


# Using the higher order function
greet_hof()  # This will execute the inner function but not return it


a_hof = func_hof(greet_hof)  # Calls the greet_hof function through func_hof
print(a_hof)  # This will print the inner function

# Decorators - a way to modify or enhance the behavior of a function without changing its code


def my_decorator(func):
    def wrap_func():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrap_func


@my_decorator
def display():
    print("Display function executed!")

# The @my_decorator syntax is a shorthand for:
# display = my_decorator(display)
# It wraps the display function with my_decorator, modifying its behavior.


# Manually wrapping the display function
display_second = my_decorator(display)
display_second()  # Calls the wrapped display function


@my_decorator
def bye():
    print("see you later")


display()  # Calls the display function, which is now wrapped by my_decorator
bye()  # Calls the bye function, which is also wrapped by my_decorator

# Calls the wrapped bye function directly - like manually wrapping it
my_decorator(bye)()

# Decorators with arguments


def my_decorator_with_args(func):
    def wrap_func(*args, **kwargs):
        print("Something is happening before the function is called with args:",
              args, "and kwargs:", kwargs)
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrap_func


@my_decorator_with_args
def greet_with_args(name, age, good):
    print(
        f"Hello {name}, you are {age} years old and you are doing great! {good} ;) Keep it going! Yeyyy")


# Calls the wrapped function with arguments
greet_with_args("Lewy", 26, good="Yesss")
