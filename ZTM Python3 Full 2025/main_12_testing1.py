def do_stuff(number):
    try:
        number = int(number)
        print(f"Doing stuff with {number}...")
        return number * 3
    except ValueError as err:
        return err
