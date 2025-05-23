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

    # Constructor, # self - to refer to the instance of the class #  __init__ dunder method
    def __init__(self, name, age):
        if (age > 18):
            self._name = name  # instance attribute
            self._age = age  # _protected instance attribute private?

    def _shout(self):  # instance method
        print(f'My name is {self._name}')

    def _run(self, hello):
        print(f'Running {hello}...')

# classmethod - to create a method that is bound to the class and not the instance of the class
# staticmethod - to create a method that is bound to the class and not the instance of the class

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)  # cls - to refer to the class itself

    @staticmethod
    def static_hello(hello):
        print(f'Hello {hello}, here is a static method')


player1 = PlayerCharacter("John", 25)
player2 = PlayerCharacter("Jane", 22)
player2._power = 99

print(player1._name)
print(player2._shout())
print(player1._run("GoodYeyyy"))
print(player2._power)

player3 = PlayerCharacter.adding_things(10, 20)
print(player3._name, player3._age)
