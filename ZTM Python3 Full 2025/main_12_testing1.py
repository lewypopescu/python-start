def do_stuff(number=0):
    try:
        if number:
            number = int(number)
            print(f"Doing stuff with {number}...")
            return number * 3
        else:
            return "plese provide a number"
    except ValueError as err:
        return err
