#1.Write a for loop to print numbers from 1 to 10.
for i in range(1,11):
    print(i)

#2. String Iteration:Write a program that counts vowels in a string.
def count_vowels(string):
    vowels = "aeiouAEIOU"  
    count = 0
    for char in string:  
        if char in vowels:  
            count += 1  
    return count
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))

#3.Accumulator Pattern: Calculate the sum of squares from 1 to 100
sum_of_squares = 0  
for num in range(1, 101):  
    sum_of_squares = sum_of_squares + (num * num) 
print("Sum of squares from 1 to 100 is:", sum_of_squares)

#4.Nested Loops: Create a multiplication table up to 10x10.
for i in range(1, 11):  
    for j in range(1, 11):  
        print(i * j, end="\t") 
    print() 

#5.Image Processing: Use PIL to invert the colors of an image.
from PIL import Image, ImageOps

# Open an image
image = Image.open("C:\\Users\\palak\\Downloads\\ROSE.jpeg")  # Replace with your image file

# Invert the colors
inverted_image = ImageOps.invert(image.convert("RGB"))

# Save and show the result
inverted_image.save("C:\\Users\\palak\\Downloads\\ROSE.jpeg")
inverted_image.show()





