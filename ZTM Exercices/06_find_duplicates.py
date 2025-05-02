some_list = ["a", "a", "b", "c", "d", "e", "e", "e", "f", "g", "h", "i"]

duplicates = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
            