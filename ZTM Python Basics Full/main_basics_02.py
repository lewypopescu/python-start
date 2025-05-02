#conditional logic & #indentation

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
print('Always print me!') # This will always print
if is_good and is_awesome:
    print('You are awesome and good!')
elif is_good or is_awesome:
    print('You are good or awesome!')
else:
    print('You are neither good nor awesome!')
print('Always print me!') # This will always print

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
print('You are awesome!' if is_awesome else 'You are not awesome!') if is_good else print('You are neither good nor awesome!')

#truthy vs falsy !!!

# 0, '', [], {}, None are falsy
# everything else is truthy
#truthy
print(bool(1)) # True
print(bool('True')) # True
print(bool('False')) # True
#falsy
print(bool(0)) # False
print(bool('')) # False
print(bool([])) # False
print(bool({})) # False
print(bool(None)) # False
#truthy vs falsy with lists
print(bool([1, 2, 3])) # True
print(bool([''])) # True    
print(bool([0])) # True
print(bool([None])) # True
print(bool([False])) # True
print(bool([True])) # True
print(bool([0, 1, 2])) # True
print(bool([None, 0, ''])) # True

#logical operators
# and, or, not
# and
print("a" < "b" and 1 < 2) # True
print("a" < "A") # False
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
# or
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(5 < 10 and 10 > 5) # True
print(5 < 10 or 10 > 5) # True

# not
print(not True) # False
print(not False) # True
print(not (5 < 10)) # False
print(not (5 > 10)) # True

# is vs ==
# is checks if two variables point to the same object
# == checks if two variables have the same value
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # False
print(a == b) # True
# is not
print(a is not b) # True
print(a != b) # False
# in
print(1 in a) # True
print(4 in a) # False
print(1 not in a) # False
print(True is True) # True
print(False is False) # True
print("1" is "1") # True
print([1, 2, 3] is [1, 2, 3]) # False
print(10 is 10) # True
print([] is []) # False

# for loops
for i in range(10):
    print(i)

for item in (1, 2, 3, 4, 5):
    for x in ["a", "b", "c"]:
        print(item, x)

for item in "hello world":
    print(item)

#iterables
#iterable - list, dictionary, set, tuple, string
#iterate - to go through each item in an iterable, operate on each item, one by one
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

#range
#range(start, stop, step)
for i in range(0, 10, 2):
    print(i)
for i in range(10, 0, -1):
    print(i)
for i in range(3):
    print(list(range(9)))

#enumerate
#enumerate(iterable, start=0)
#enumerate - to get the index and value of each item in an iterable
for i, char in enumerate("hello world"):
    print(i, char)
for i, char in enumerate("hello world", start=3):
    print(i, char)
for i, item in enumerate(list(range(30))):
    if item == 20:
        print(f"index of 20 is {i}")

#while loops
#while loops - to repeat a block of code while a condition is true
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

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("doneee")

#break, continue, pass
#break - to exit a loop
#continue - to skip the current iteration and move to the next iteration
#pass - to do nothing, just a placeholder, to avoid syntax errors, maybe something will be added later