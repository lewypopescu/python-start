# Error Handling
# try/except
# They are many built-in exceptions in Python, such as ZeroDivisionError, TypeError, ValueError, etc.

# This function attempts to divide two numbers and handles potential errors.
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print(f"Error: {e}. Cannot divide by zero.")
        return None
    except TypeError as e:
        print(f"Error: {e}. Please provide numbers.")
        return None
    else:
        return result
    finally:
        print("Execution completed of first try/except block.")


# Example usage
result1 = divide_numbers(10, 2)
result2 = divide_numbers(10, 0)
result3 = divide_numbers(10, 'a')

# Error handling is crucial for writing robust and user-friendly applications. See this full while loop in Exercices/16_error_handling.py for a more complex example.

while True:
    try:
        input_number = int(input("Enter a number: "))
        result_ok = 9 / input_number
        # This will raise a generic Exception intentionally
        raise Exception("hey cut it out")
        raise ValueError(
            "This is a custom error message for demonstration purposes: hey cut it out")  # This will raise a ValueError intentionally

    except ZeroDivisionError as err:
        print(f"Error: {err}. Cannot divide by zero.")
        break  # Break the loop if division by zero occurs
    # except can always be used for more than one exception, but it is better to use specific exceptions to handle different errors
    else:
        print("You entered a valid number. Good job!")
        print(f"Result: {result_ok}")
    finally:
        print(
            "finally: This will always execute, regardless of whether an exception occurred or not.")
    print("End of the loop iteration. If else have break in it of continue, it will not execute this line, because continue will skip to the next iteration and break will exit the loop.")

# Go Go Go, no errors can stop us! :d
