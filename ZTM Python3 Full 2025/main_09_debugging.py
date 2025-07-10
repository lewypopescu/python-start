# Debugging is the process of finding and fixing errors in your code.
# It is an essential skill for any programmer to master.
# Debugging can be done using various techniques, including print statements, logging, and debugging tools.
# Debugging tools like IDEs (Integrated Development Environments) often have built-in debuggers that allow you to set breakpoints, step through code, and inspect variables.

# Common debugging techniques include:
# 1. Print Statements: Inserting print statements to check the values of variables at different points in the code.
# 2. Logging: Using the logging module to log messages at different levels (debug, info, warning, error).
# 3. Debugging Tools: Using IDEs or debugging tools to step through the code, set breakpoints, and inspect variables.
# 4. Exception Handling: Using try-except blocks to catch and handle exceptions gracefully.
# 5. Code Review: Reviewing code with peers to identify potential issues.
# 6. Rubber Duck Debugging: Explaining your code or problem to someone else (or even to an inanimate object) to gain clarity.
# 7. Unit Testing: Writing tests to ensure that individual components of your code work as expected.
# 8. Profiling: Analyzing the performance of your code to identify bottlenecks.
# 9. Version Control: Using version control systems (like Git) to track changes and revert to previous versions if necessary.
# 10. Documentation: Writing clear documentation to help understand the code and its intended behavior.

# Linting is the process of checking your code for potential errors, stylistic issues, and adherence to coding standards without executing it. It helps maintain code quality and readability.

# Common linting tools include:
# 1. Pylint: A widely used Python linter that checks for errors, enforces coding standards, and suggests improvements.
# 2. Flake8: A tool that checks for style guide enforcement and programming errors.
# 3. Black: A code formatter that automatically formats Python code to adhere to PEP 8 standards.
# 4. MyPy: A static type checker for Python that checks type annotations and ensures type correctness.
# 5. Pyflakes: A simple tool that checks Python code for errors without enforcing style.

# Read Errors:
# 1. SyntaxError: Raised when there is a syntax error in the code, such as a missing colon or unmatched parentheses.
# 2. IndentationError: Raised when there is an indentation error in the code, such as inconsistent indentation levels.
# 3. NameError: Raised when a variable or function is not defined or is misspelled.
# 4. TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# 5. ValueError: Raised when a function receives an argument of the right type but an inappropriate value.
# 6. IndexError: Raised when trying to access an index that is out of range for a list or tuple.
# 7. KeyError: Raised when trying to access a dictionary key that does not exist.
# 8. AttributeError: Raised when trying to access an attribute or method that does not exist on an object.
# 9. ImportError: Raised when a module or package cannot be imported.
# 10. ZeroDivisionError: Raised when trying to divide by zero.

# Debugging is an essential skill for any programmer, and mastering it can significantly improve your coding efficiency and code quality.

# PDB (Python Debugger) is a built-in module in Python that provides an interactive debugging environment. It allows you to set breakpoints, step through code, inspect variables, and evaluate expressions.

import pdb


def buggy_function():
    a = 10
    b = 0
    c = a / b  # This will raise a ZeroDivisionError
    return c


try:
    buggy_function()
except ZeroDivisionError as err:
    print("An error occurred:", err)
    pdb.set_trace()

# The pdb.set_trace() function sets a breakpoint in the code, allowing you to inspect the state of the program at that point.
# You can then use commands like 'n' (next), 'c' (continue), 'q' (quit), and others to navigate through the code.
# To use PDB, you can run your script with the `-m pdb` option:
# python -m pdb your_script.py
# Alternatively, you can insert `pdb.set_trace()` directly in your code where you want to start debugging. You can also write code in the pdb shell to inspect variables, evaluate expressions, and control the flow of execution.
# After you finish debugging, you can remove the `pdb.set_trace()` line from your code.
