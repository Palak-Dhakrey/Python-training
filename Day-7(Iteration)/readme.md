# Iteration: Notes and Assignment

## 6.1. Introduction: Iteration
Iteration is the process of repeatedly executing a set of instructions. In Python, this is commonly done using loops.

## 6.2. The for Loop
A `for` loop iterates over a sequence (list, string, or range):
```python
for item in [1, 2, 3]:
    print(item)
```

## 6.3. Flow of Execution of the for Loop
1. Initialize loop variable.
2. Execute loop body.
3. Move to the next item until the sequence is exhausted.

## 6.4. Strings and for Loops
Strings are iterable:
```python
for char in "Python":
    print(char)
```

## 6.5. Lists and for Loops
Iterate through lists or use `range()`:
```python
for i in range(5):
    print(i)
```

### 6.5.2. Using Loops in Turtle Graphics
```python
import turtle
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)
```

## 6.6. The Accumulator Pattern
Accumulates values during iteration:
```python
total = 0
for i in range(5):
    total += i
print(total)  # Output: 10
```

## 6.7. Traversal and for Loop: By Index
Use `range(len())` for index-based iteration:
```python
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])
```

## 6.8. Nested Iteration: Image Processing
Images are processed using nested loops.

### 6.8.1. The RGB Color Model
Each pixel has Red, Green, and Blue (RGB) values.

### 6.8.2. Image Objects
Use Pillow (PIL) for image handling:
```python
from PIL import Image
img = Image.open('example.jpg')
```

### 6.8.3. Image Processing with Nested Loops
```python
width, height = img.size
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        img.putpixel((x, y), (255 - r, 255 - g, 255 - b))  # Invert colors
```

## 6.9. Debugging with Intermediate Results
Use print statements:
```python
for i in range(5):
    print(f"i: {i}")
```

## 6.10. Naming Variables in For Loops
Use meaningful names:
```python
for student in students:
    print(student)
```

## 6.11. Understanding Iterables
An iterable is any object that returns elements one by one (lists, tuples, strings, dictionaries).

## 6.12. Tracking Iterator Variables
Use `enumerate()` to keep track of index:
```python
students = ["Alice", "Bob", "Charlie"]
for index, student in enumerate(students):
    print(index, student)