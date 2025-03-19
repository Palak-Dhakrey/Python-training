#1.Fix the circular import problem between module_a.py and module_b.py.
'''module_a.py:
import module_b

def func_a():
    return "Function A"

print(module_b.func_b())
module_b.py:
import module_a

def func_b():
    return "Function B"'''
#SOLUTION:
def func_a():
    return "Function A"
def call_func_b():
    import module_b  # Import inside the function to break circular dependency
    print(module_b.func_b())  # Calls func_b() from module_b
call_func_b()  # Call the function once (NO RECURSION)
def func_b():
    return "Function B"

#2.Write a program that dynamically imports and executes a function from any module specified by the user. Example:
'''Enter module name: math
Enter function name: sqrt
Enter argument: 25
Output: 5.0'''
#SOLUTION:
import importlib
def dynamic_function_call():
    module_name = input("Enter module name: ")
    function_name = input("Enter function name: ")
    argument = input("Enter argument: ")
    try:
        # Dynamically import module
        module = importlib.import_module(module_name)
        # Retrieve function from module
        func = getattr(module, function_name)
        # Convert argument to correct type (supports only numbers for simplicity)
        if argument.isdigit():
            argument = int(argument)
        else:
            try:
                argument = float(argument)
            except ValueError:
                pass  # Keep it as string if it cannot be converted
        # Execute function and print result
        result = func(argument)
        print("Output:", result)
    except ModuleNotFoundError:
        print("Error: Module not found.")
    except AttributeError:
        print("Error: Function not found in module.")
    except Exception as e:
        print(f"Error executing function: {e}")
# Run the program
dynamic_function_call()

#3.Create a custom module calculator.py that handles division by zero and invalid inputs gracefully.
''' calculator.py
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"
Import and use this module.'''
#SOLUTION:
# calculator.py
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"
# main.py
import calculator
a = input("Enter first number: ")
b = input("Enter second number: ")
try:
    a = float(a)
    b = float(b)
    result = calculator.divide(a, b)
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")
#4. Advanced Import Strategies
'''Write a script that:
Imports a module.
Checks if a function exists.
Executes it if available, otherwise gracefully handles the error.'''
#CODE:
# calculator.py
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"
# main.py
import calculator
import importlib
def execute_function(module_name, function_name, *args):
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, function_name):
            func = getattr(module, function_name)
            return func(*args)
        else:
            return f"Error: Function '{function_name}' not found in module '{module_name}'."
    except ModuleNotFoundError:
        return f"Error: Module '{module_name}' not found."
    except Exception as e:
        return f"Error: {e}"
a = input("Enter first number: ")
b = input("Enter second number: ")
try:
    a = float(a)
    b = float(b)
    result = execute_function("calculator", "divide", a, b)
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")
#5.Use time module to measure import time for different methods (single import vs. importing everything).
'''import time
start = time.time()
import math
end = time.time()
print(f"Import time: {end - start}")'''
# calculator.py
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"
# main.py
import time
start = time.time()
import calculator
import importlib
end = time.time()
print(f"Import time: {end - start}")
def execute_function(module_name, function_name, *args):
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, function_name):
            func = getattr(module, function_name)
            return func(*args)
        else:
            return f"Error: Function '{function_name}' not found in module '{module_name}'."
    except ModuleNotFoundError:
        return f"Error: Module '{module_name}' not found."
    except Exception as e:
        return f"Error: {e}"
a = input("Enter first number: ")
b = input("Enter second number: ")
try:
    a = float(a)
    b = float(b)
    result = execute_function("calculator", "divide", a, b)
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")
#6. Module Creation and Distribution
'''Create a Python package structure with __init__.py.
Write a setup.py to make it installable.
Install your package locally.
Import and test your package.'''
from .calculator import divide
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"
from setuptools import setup, find_packages
setup(
    name="my_calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Your Name",
    author_email="your_email@example.com",
    description="A simple calculator package",
    url="https://github.com/yourusername/my_calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
import my_calculator
print(my_calculator.divide(10, 2))  # Output: 5.0
print(my_calculator.divide(10, 0))  # Output: Cannot divide by zero.
#7.Explore sys.path and add a custom directory to import modules from an unconventional path.
'''import sys
sys.path.append('/custom/path/to/modules')
import mymodule'''
import sys
print("\n".join(sys.path))
import sys
sys.path.append("C:/custom/path/to/modules")  # Use a valid directory path
import mymodule  # Import your module
print(dir(mymodule))  # Lists available functions and attributes in mymodule
#8.Write a unit test for a function that imports a module. Use unittest.mock to mock the imported module.
'''from unittest import mock
with mock.patch('math.sqrt', return_value=100):
    print(math.sqrt(25))  # Should print 100'''
import unittest
from unittest import mock
import calculator  # Import the module containing the function
class TestCalculator(unittest.TestCase):
        @mock.patch('calculator.math.sqrt', return_value=100)  # Mocking math.sqrt
        def test_calculate_square_root(self, mock_sqrt):
         result = calculator.calculate_square_root(25)
        self.assertEqual(result, 100)  # Expect mocked value (100)
        # Ensure math.sqrt was called with 25
        mock_sqrt.assert_called_once_with(25)
if __name__ == '__main__':
    unittest.main()

#9.Investigate modules that run code at import time. Create a module that prints something as soon as it’s imported.
#print("This runs on import!")
print("This runs on import!")
def greet():
    return "Hello from auto_run!"
import auto_run
if __name__ == "__main__":
    print("This runs only when executed directly!")

#10.Explore sys.modules to understand how Python caches imports and how to reload modules.
import sys
import mymodule  # Import your custom module
print(sys.modules['mymodule'])  # Prints the cached module reference
if 'mymodule' in sys.modules:
    print("mymodule is already loaded!")
else:
    print("mymodule is not loaded!")
import importlib
importlib.reload(mymodule)  # Forces Python to reload the module
del sys.modules['mymodule']
import mymodule  # Now it reloads completely













    
