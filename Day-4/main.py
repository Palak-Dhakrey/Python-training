#3. CODE
text = "Palak"
print(text[0])  # Output: P
print(text[-1]) # Output: k (Negative indexing)
#4.Write code to access the last character of a string
text = "Payal"
print(text[-1])  # Output: l
#5.Create a list of numbers and access the third element
numbers = [10, 20, 30, 40, 50]
print(numbers[2])  # Output: 30
#6.What is the result of len([1, [2, 3], 4]) and why?
'''Output: 3
Explanation: The list contains three elements (1, [2,3], 4), and [2,3] is a single element'''
#7.Explain slicing with a practical example
text = "Hello, World!"
print(text[0:5])  # Output: Hello,st = 0 end = 5-1
'''Slicing is used to extract a portion of a sequence (like a list, string, or tuple) 
by specifying a start, stop, and step.
syntax:sequence[start:stop:step]
'''
#8.How would you reverse a string using slicing?
text = "Python"
print(text[::-1])  # Output: nohtyP
#9.Demonstrate list concatenation and repetition with examples.
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)    # Concatenation → [1, 2, 3, 4, 5, 6]
print(a * 2)    # Repetition → [1, 2, 3, 1, 2, 3]
#10.Write code to count the occurrences of an element in a list
lst = [1, 2, 2, 3, 2]
print(lst.count(2))  # 3
#11.What will my_tuple = (1, 2, 3); print(my_tuple[1:]) output?
my_tuple = (1, 2, 3)
print(my_tuple[1:])  # (2, 3)
#12.Difference Between append() and extend()
'''append(x): Adds a single element to the list.
extend(iterable): Adds elements of an iterable to the list.'''
lst = [1, 2]
lst.append([3, 4])
print(lst)  # [1, 2, [3, 4]]
lst = [1, 2]
lst.extend([3, 4])
print(lst)  # [1, 2, 3, 4]
#13.Write code to split the sentence: "Learn Python, step by step!" into words.
sentence = "Learn Python, step by step!"
print(sentence.split())  # ['Learn', 'Python,', 'step', 'by', 'step!']
#14.Join a list ['Python', 'is', 'fun'] into a single string.
words = ['Python', 'is', 'fun']
print(" ".join(words))  # 'Python is fun'
#15.Given a list numbers = [1, 2, 2, 3, 4, 2], find the index of the first 2.
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.index(2))  # 1
#16.Write code to check if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))  # True
#17.Implement a function that returns the length of the longest word in a sentence.
def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return len(longest)
print(longest_word("Python is amazing"))  # 7
#18.Demonstrate nested list indexing.
nested = [[1, 2], [3, 4, [5, 6]]]
print(nested[1][2][1])  # 6
#19.How do you convert a list of characters into a string?
chars = ['H', 'e', 'l', 'l', 'o']
print("".join(chars))  # 'Hello'
#20.Write code to remove duplicates from a list while preserving order.
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
print(remove_duplicates([1, 2, 2, 3, 4, 3]))  # Output: [1, 2, 3, 4]
#21.Write a function that takes a list of tuples and sorts it by the second element of each tuple.
def sort_by_second(tuples):
    return sorted(tuples, key=lambda x: x[1])
print(sort_by_second([(1, 3), (2, 1), (3, 2)]))  # [(2, 1), (3, 2), (1, 3)]
#22.Implement a program to flatten a nested list of arbitrary depth.
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
print(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]
#23.Create a function that rotates a list to the right by k steps
def rotate(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]
print(rotate([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
#24.Given two strings, write a function that returns True if they are anagrams.
from collections import Counter
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_anagram("listen", "silent"))  # True
#25.Create a function to split a list into chunks of a specified size.
def chunk_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]
print(chunk_list([1, 2, 3, 4, 5, 6], 2))  # [[1, 2], [3, 4], [5, 6]]
#26.Implement a function that merges two sorted lists into one sorted list
def merge_sorted(lst1, lst2):
    return sorted(lst1 + lst2)
print(merge_sorted([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]













