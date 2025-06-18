from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time = end_time - start_time
        print(f"execution time: {execution_time} seconds")
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 9


long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    "name": "Go",
    # changing this will either run or not run the message_friends function.
    "valid": True,
}


def authenticated(fn):
    # code here
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")

    return wrapper


@authenticated
def message_friends(user):
    print(f"message has been sent {user['name']}")


message_friends(user1)
# If user1['valid'] is False, the message_friends function will not run.
message_friends({"name": "Go not yet", "valid": False})
