while True:
    try:
        input_number = int(input("Enter a number: "))
        result_ok = 9 / input_number
    except ValueError as err:
        print(f"Error: {err}. Please enter a valid number.")
        continue  # Continue to the next iteration of the loop
    except ValueError as err:
        print(
            f"Error: {err}. aaaaaaaaa; will always go for the first except ValueError :).")
    except ZeroDivisionError as err:
        print(f"Error: {err}. Cannot divide by zero.")
        break  # Break the loop if division by zero occurs
    # except can always be used for more than one exception, but it is better to use specific exceptions to handle different errors:
    except (ValueError, ZeroDivisionError) as err:
        print(f"Error: {err}. hello world ???")
    else:
        print("You entered a valid number. Good job!")
        print(f"Result: {result_ok}")
    finally:
        print(
            "finally: This will always execute, regardless of whether an exception occurred or not.")
    print("End of the loop iteration. If else have break in it of continue, it will not execute this line, because continue will skip to the next iteration and break will exit the loop.")
