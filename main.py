
'''3. **Exercise:**
   - Create a Python script that demonstrates:
     - Addition, subtraction, multiplication, and division.
     - Comparisons between numbers.
     - Logical operations like `and`, `or`, `not`.'''

# Addition
a = 10
b = 5
sum_result = a + b
print("Addition:", sum_result)

# Subtraction
sub_result = a - b
print("Subtraction:", sub_result)

# Multiplication
mul_result = a * b
print("Multiplication:", mul_result)

# Division
div_result = a / b
print("Division:", div_result)

# 3.2 Comparison Operations
x = 8
y = 3
print("x > y:", x > y)   # Greater than
print("x < y:", x < y)   # Less than
print("x == y:", x == y) # Equal to
print("x != y:", x != y) # Not equal to

# 3.3 Logical Operations
a = True
b = False

print("a and b:", a and b)  # True if both are True
print("a or b:", a or b)    # True if at least one is True
print("not a:", not a)      # Inverts the value of a

#Write a program that uses built-in functions inside expressions:
numbers = [5, 3, 8, 1]
print(max(numbers) - min(numbers))

#Convert variables between types and observe the results:
x = 10
print("Initial Values:")
x = 20
print("Updated Values:")
#Rewrite a piece of code with meaningful variable names
# original code
def f(a, b):
    c = a * 3.14 * b
    return c

x = 5
y = 10
z = f(x, y)
print(z)
#rewritten code
def calculate_circumference(radius, multiplier):
    circumference = radius * 3.14 * multiplier
    return circumference

radius_value = 5
multiplier_value = 10
result = calculate_circumference(radius_value, multiplier_value)
print(result)

#Identify statements and expressions in this code:
x = 5 + 3   #expression
print(x)    #statement

#Write expressions using multiple operators to explore Python’s order of operations.
result = 2 + 3 * 4 ** 2 / 8
print(result)

#Assign a value to a variable, reassign it, and observe the changes:
count = 10
print(count)
count = 20
print(count)

#Increment and decrement variables using `+=` and `-=`.
score = 100
score += 10
print(score)
score -= 5
print(score)






