# Square
my_list = [1, 2, 3, 4, 5, 6]

print(list(map(lambda x: x ** 2, my_list)))

# List of tuples
my_tuples = [(1, 1), (3, 2), (5, -1), (10, 6)]

# Sort by second element of each tuple
my_tuples.sort(key=lambda x: x[1])
print(my_tuples)

print(sorted(my_tuples, key=lambda x: x[1]))
