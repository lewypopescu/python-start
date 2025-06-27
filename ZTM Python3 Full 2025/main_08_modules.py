# Modules - importing and using modules

import main_08_test_modules

# from main_08_test_modules import * # Importing all functions from the module

from main_08_test_package import shopping_cart

import random
# import random as lalala # Importing the random module with an alias


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
