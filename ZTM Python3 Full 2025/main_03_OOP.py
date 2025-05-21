# OOP
# Object Oriented Programming
# Class - Object - Method - Attribute
# Encapsulation - Inheritance - Polymorphism
# Class - A blueprint for creating objects
# Object - An instance of a class
# Method - A function defined inside a class
# Attribute - A variable defined inside a class
# Encapsulation - The bundling of data and methods that operate on that data within one unit
# Inheritance - The ability to create a new class that is based on an existing class
# Polymorphism - The ability to use the same method name for different types of objects


class PlayerCharacter:

    membership = True  # Class Object Attribute

    def __init__(self, name, age):  # Constructor
        if (age > 18):
            self.name = name  # instance attribute
            self.age = age

    def shout(self):  # instance method
        print(f'My name is {self.name}')

    def run(self, hello):
        print(f'Running {hello}...')


player1 = PlayerCharacter("John", 25)
player2 = PlayerCharacter("Jane", 22)
player2.power = 99

print(player1.name)
print(player2.shout())
print(player1.run("GoodYeyyy"))
print(player2.power)
