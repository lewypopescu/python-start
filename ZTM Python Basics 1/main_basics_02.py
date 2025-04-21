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

