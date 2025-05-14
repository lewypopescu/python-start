name = input("What is your favorite color?")
print("hellooo   " + "9" + name)

#int
#float
#bool
#str
#list
#tuple
#set
#dict

#Classes -> custom types

#Specialized Data Types
#None

#Modules

#Fundamental Data Types
#int and float

print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))

print(2 ** 3)
print(5 // 4)
print(6 % 4)

#math functions

print(round(3.9))
print(abs(-20))

#operator precedence

print((20 - 3) + 2 ** 4)

# ()
# **
# * /
# + -

#bin() and complex

print(bin(5))
print(int('0b101', 2))

#variables

iq = 190
user_age = iq/4
a = user_age
print(a)

#constants
PI = 3.14
a,b,c = 1,2,3
print(a)
print(b)
print(c)

#augmented assignment operator
some_value = 5
some_value = some_value + 2
print(some_value)
some_value += 2
print(some_value)
some_value -= 2
print(some_value)
some_value *= 2
print(some_value)

#str
print(type("hi hello there 24!"))
username = 'developer'
password = 'superwowww'
long_string = '''
WOWwwwWWW
O O
---
'''
print(long_string)
first_name = 'Lewy'
last_name = 'Popescu'
full_name = first_name + ' ' + last_name
print(full_name)

#string concatenation
print('hello' + ' Lewy')
print(type(int(str(100))))

#type conversion
a = str(100)
b = int(a)
c = type(b)
print(c)

#escape sequence
weather = "a"
weather = "\t It\'s \"kind of\" sunny \n hope you have a lovely day!\n heyyy heyyy"
print(weather)

#formatted strings
name = 'Lewy'
age = 26
print('hi ' + name + '. You are ' + str(age) + ' years old')
print(f'hi {name}. You are {age} years old')
print('hi {}. You are {} years old'.format('hello', '99'))
print('hi {}. You are {} years old'.format(name, age))
print('hi {1}. You are {0} years old'.format(name, age))
print('hi {new_name}. You are {age} years old'.format(new_name='hey', age=99))

#string indexes
selfish = '01234567'
# [start:stop:stepover]
print(selfish[0:8:2])
print(selfish[:5])
print(selfish[::1])
print(selfish[-1])
print(selfish[-4])
print(selfish[::-1])
print(selfish[::-2])

#built-in functions + methods
print(len('helloooo'))
greet = 'helloooo'
print(greet[0:len(greet)])
quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))
print(quote)
quote2 = quote.replace('be', 'me')
print(quote2)

#booleans
name = 'Lewy'
is_cool = False
is_cool = True
print(bool(1))
print(bool(0))
print(bool('True'))
print(bool('False'))

 #lists
li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2,'a', True]
print(li3)

#list slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart[0:2])
print(amazon_cart[0::2])
print(amazon_cart[::-1])

#list methods
print(len(amazon_cart))
amazon_cart.append('laptop')
print(amazon_cart)
amazon_cart.insert(2, 'laptop')
print(amazon_cart)
amazon_cart.extend('aaa')
print(amazon_cart)
amazon_cart.extend(['aaaa'])
print(amazon_cart)
amazon_cart.pop()

#common list patterns
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
basket.reverse()
print(basket[::-1])
print(basket)
print(list(range(1, 100)))
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
new_sentence1 = ' '.join(['hi', 'my', 'name', 'is', 'JOJO'])

#list unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(other)
print(d)

#dictionaries
my_dict = {
    'a': [1, 2, 3],
    'b': 2,
    'x': True,
}

print(my_dict['a'][1])
print(my_dict ['b'] + my_dict['x'])

#dictionary methods
user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user.get('age', 55))
print('basket' in user)
print('age' in user.keys())
print('hello' in user.values())
print(user.items())
print(user.keys())
print(user.values())
print(user.pop('age'))
print(user)
print(user.popitem())

#tuples
coordinates = (1, 1, 1, 1, 2, 3)
print(coordinates[0])
print(coordinates[0:2])
print(coordinates[::-1])

#tuples methods
print(coordinates.count(1))
print(coordinates.index(2))
print(1 in coordinates)
print(3 in coordinates)
print(len(coordinates))
x, y, z, *other = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(x)
print(other)

#sets
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))
print(my_set.add(100))
print(my_set)
print(my_set.pop())
print(my_set)
print(my_set)
print(my_set.discard(2))
print(my_set)
new_set = my_set.copy()
print(new_set)
my_set.clear()
print(my_set)
print(new_set)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(set(list))
print(set('hello world'))
your_set = {4, 5, 6, 7, 8, 9}
print(my_set.union(your_set))
print(my_set.intersection(your_set))
print(my_set.difference(your_set))
print(my_set.difference_update(your_set))
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))
print(my_set.isdisjoint(your_set))

#frozen set
my_set4 = frozenset({1, 2, 3, 4, 5})
print(my_set4)



#Yeyyy good joob, Lewy! :x



