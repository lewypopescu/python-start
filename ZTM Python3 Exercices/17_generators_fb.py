def fib_num(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b
        # This will print the index of the current iteration
        print(f"index of the current iteration: {i}")


for x in fib_num(9):
    print(x)


def fib_num_list(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
        # This will print the index of the current iteration
        print(f"index of the current iteration: {i}")
    return result


print(fib_num_list(9))
