def highest_even(list):
    result = 0
    for i in list:
        if i % 2 == 0 and i > result:
            result = i
    return result

print(highest_even([1, 22, 88, 4, 5, 6, 7, 8, 9, 44]))