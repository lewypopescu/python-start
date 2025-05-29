# OOP
# Object Oriented Programming
# Class - Object - Method - Attribute
# Encapsulation - Abstraction - Inheritance - Polymorphism
# Class - A blueprint for creating objects
# Object - An instance of a class
# Method - A function defined inside a class
# Attribute - A variable defined inside a class
# Encapsulation - The bundling of data and methods that operate on that data within one unit
# Abstraction - The process of hiding the complex implementation details and showing only the essential features of the object
# Inheritance - The ability to create a new class that is based on an existing class
# Polymorphism - The ability to use the same method name for different types of objects

class SignIn(object):  # Base class, object is the parent class of all classes in Python, from there comes all the methods and attributes
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_in(self, username, password):
        self.username = username
        self.password = password
        print(f"Signing in {self.username} with password {self.password}")

    def _run(self, hello):
        print(f'Running Sign in run {hello}...')


class PlayerCharacter(SignIn):  # Inheritance

    membership = True  # Class Object Attribute

    # Constructor, # self - to refer to the instance of the class #  __init__ dunder method
    def __init__(self, name, age, username="", password=""):
        if (age > 18):
            super().__init__(username, password)
            self._name = name  # instance attribute
            self._age = age  # _protected instance attribute private?

    def _shout(self):  # instance method
        print(f'My name is {self._name}')

    def _run(self, hello):
        # Overriding the parent class method
        super()._run(hello)
        SignIn._run(self, "Sign in hereee")  # Calling the parent class method
        print(f'Running Simple run {hello}...')

# classmethod - to create a method that is bound to the class and not the instance, it can be called on the class or instance
# staticmethod - to create a method that does not depend on the instance or class, it can be called on the class or instance

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)  # cls - to refer to the class itself

    @staticmethod
    def static_hello(hello):
        print(f'Hello {hello}, here is a static method')


player1 = PlayerCharacter("John", 25, "JohnS", "1234")
player2 = PlayerCharacter("Jane", 22, "JaneS", "5678")

player2._power = 99

print(player1._name)
print(player2._shout())
print(player1._run("GoodYeyyy"))
print(player2._power)

player3 = PlayerCharacter.adding_things(10, 20)
print(player3._name, player3._age)

print(player1.username)
print(player2.password)

player1.sign_in("JohnS", "1234")
player2.sign_in("JaneS", "5678")

# isinstance - to check if an object is an instance of a class
print(isinstance(player1, PlayerCharacter))
print(isinstance(player1, SignIn))

# issubclass - to check if a class is a subclass of another class
print(issubclass(PlayerCharacter, SignIn))
print(issubclass(SignIn, PlayerCharacter))

# introspection - to check the attributes and methods of an object
print(dir(player1))  # List all attributes and methods of the player1 object
print(player1.__dict__)  # List all attributes of the player1 object

# dunder methods - to check the special methods of an object, they can be also overridden!
print(player1.__class__)  # Check the class of the player1 object
print(player1.__module__)  # Check the module of the player1 object
print(player1.__doc__)  # Check the docstring of the player1 object
# __str__ - to get a string representation of the object
print(player1.__str__())  # Get the string representation of the player1 object
# dunder methos overriding


def __str__(self):
    return f"PlayerCharacter(name={self._name}, age={self._age}, username={self.username})"


# Overriding the __str__ method of the PlayerCharacter class
PlayerCharacter.__str__ = __str__
# Get the string representation of the player1 object using the overridden __str__ method
print(player1)

# Multiple Inheritance Example


class GameUser(object):
    def sign_in(self):
        print("Signing in to the game...")

    def sign_out(self):
        print("Signing out of the game...")


class Wizard(GameUser):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} attacks with power {self.power}!")


class Archer(GameUser):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"{self.name} has {self.arrows} arrows left.")

    def shoot(self):
        if self.arrows > 0:
            print(f"{self.name} shoots an arrow!")
            self.arrows -= 1
        else:
            print(f"{self.name} has no arrows left to shoot!")

    def run(self):
        print(f"{self.name} is running super fast!")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb1 = HybridBorg("borgie", 80, 10)
hb1.sign_in()
hb1.attack()
hb1.check_arrows()
hb1.shoot()
hb1.check_arrows()
hb1.run()
hb1.sign_out()

# MRO - Method Resolution Order


class A():
    num = 9


class B(A):
    pass


class C(A):
    num = 3


class D(B, C):
    pass


# MRO for class D
print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.num)  # Output: 3, it will look for the first/last occurrence of num in the MRO, database is searched in the order of the MRO


class X:
    pass


class Y:
    pass


class Z:
    pass


class E(X, Y):
    pass


class F(Y, Z):
    pass


class M(F, E, Z):
    pass


print(M.__mro__)  # Output: (<class '__main__.M'>, <class '__main__.F'>, <class '__main__.E'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>)

# Depth First Search Algorithm !!! - MRO

# Good job Lewy ... go go go ;) 29/05/2025
