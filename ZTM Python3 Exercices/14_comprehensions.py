some_list = ["a", "b", "c", "d", "e", "b", "n", "b", "n", "b", "n"]

duplicates = list(
    set([item for item in some_list if some_list.count(item) > 1]))

print(duplicates)


duplicates_first = []

for item in some_list:
    if some_list.count(item) > 1 and item not in duplicates_first:
        duplicates_first.append(item)

print(duplicates_first)
