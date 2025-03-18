#1:Identify the type of error in the following code snippets and fix them:
for i in range(5):#Error is the colon(syntax error)
    print(i)
x = 10 / 0 #(RuntimeError)
def calculate_area(radius):
    return 2 * 3.14 * radius #(logical error)

#COORECT ONE
import math
for i in range(5): 
    print(i)
try:
    x = 10 / 0 
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
def calculate_area(radius):
    return math.pi * radius ** 2 
print(calculate_area(5)) 

#2:Debug the following function and correct the mistakes
def process_data(data):
    total = 0
    for item in data:
        total += int(item)
    return total / len(data)

print(process_data(['10', '20', 'abc', '30']))#ValueError: invalid literal for int() with base 10: 'abc'

#CORRECT CODE
def process_data(data):
    numbers = [int(item) for item in data if item.isdigit()] 
    return sum(numbers) / len(numbers) if numbers else 0  
print(process_data(['10', '20', 'abc', '30']))  

#3:You’re given a function that fails intermittently. Investigate the bug and fix it:
import random
def unreliable_function():
    number = random.choice([0, 1, 2])#ZeroDivisionError
    return 10 / number
for i in range(10):
    print(unreliable_function())
#CORRECT CODE
import random
def unreliable_function():
    number = random.choice([1, 2])  #Exclude 0
    return 10 / number
for i in range(10):
    print(unreliable_function())

#4:Refactor the following function to improve readability and add error handling:
def calculate_discount(price, discount):
    return price - (price * discount / 100)
print(calculate_discount(100, '10%'))
#CORRECT ONE
def calculate_discount(price, discount):
    try:
        # Convert discount to float if it's a string and remove '%'
        if isinstance(discount, str):
            discount = discount.replace('%', '')  # Remove '%' if present
            discount = float(discount)  # Convert to float
        
        # Validate inputs
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a positive number.")
        if not isinstance(discount, (int, float)) or not (0 <= discount <= 100):
            raise ValueError("Discount must be a number between 0 and 100.")

        # Calculate final price
        return price - (price * discount / 100)
    except ValueError as e:
        return f"Error: {e}"
#Test Cases
print(calculate_discount(100, '10%'))  # Output: 90.0
print(calculate_discount(200, 20))     # Output: 160.0
print(calculate_discount(150, 'abc'))  # Output: Error message
print(calculate_discount(-50, 10))     # Output: Error message
print(calculate_discount(100, 150))    # Output: Error message

#5:Explain the following code snippet step-by-step as if you’re teaching someone unfamiliar with coding:
numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print("Product:", result)

#This code calculates the product (multiplication) of all numbers in the list [1, 2, 3, 4, 5] and prints the result.
#creating a list:A list called numbers is created.
#It contains five values: [1, 2, 3, 4, 5].
#Initialising a variable:A variable named result is initialized with the value 1.
#This variable will be used to store the product of all the numbers
#looping through the list:A for loop goes through each number in the numbers list.
#num takes each value from the list one by one.
#result *= num is shorthand for result = result * num, which multiplies result by the current number.
#printing the final result:After the loop finishes, the final value of result is printed.

#6:Fix the race condition in the following code:
import threading
counter = 0
def increment():
    global counter
    for _ in range(100000):
        counter += 1
threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("Counter:", counter)  # Expected: 200000

#CORRECT ONE:
import threading
counter = 0
lock = threading.Lock()  # Create a lock
def increment():
    global counter
    for _ in range(100000):
        with lock:  # Ensure only one thread modifies counter at a time
            counter += 1
threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("Counter:", counter)  # Expected: 200000

#7:Learn to use breakpoints in your IDE (e.g., VSCode, PyCharm) to inspect variable states step-by-step
def divide(a, b):
    result = a / b
    return result

a = 10
b = 0
print(divide(a, b))
#CORRECT CODE
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    result = a / b  # Breakpoint here
    return result
a = 10
b = 0
print(divide(a, b))

#8:Optimize the following code and fix potential memory leaks
import time
def inefficient_function():
    result = []
    for i in range(100000):
        result.append(i * 2)
    time.sleep(2)
    return result
print(len(inefficient_function()))
#CORRECT ONE:
import time
def efficient_function():
    for i in range(100000):
        yield i * 2 
count = sum(1 for _ in efficient_function())
time.sleep(2)  # Sleep if necessary
print("Count:", count) 
#ALTERNATE ONE:
def efficient_function():
    return [i * 2 for i in range(100000)]
print(len(efficient_function()))

#9:Debug why the function returns None
def add(a, b):
    result = a + b
print(add(3, 4))
#The function calculates a + b, but does not return the result.
#Since no return statement is present, Python automatically returns None
#CORRECT ONE:
def add(a, b):
    return a + b  # Return the sum directly
print(add(3, 4))  # Output: 7

#10:Identify why the code doesn't raise an error:
try:
    result = 10 / 0
except:
    pass
print("No error detected!")
#The except: block does nothing, so the program continues execution without printing or logging the error.
#CORRECT ONE:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")  # Now, the error is handled



    





