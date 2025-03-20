1. Define a sequence.What types of sequences exist in Python?
ANS:A sequence is an ordered collection of elements that can be accessed using indexing.
Types of sequences in Python:
Lists (list) - Mutable, ordered collection.
Tuples (tuple) - Immutable, ordered collection.
Strings (str) - Immutable sequence of characters.
Ranges (range) - Immutable sequence of numbers.
Bytes (bytes) - Immutable sequence of integers (0-255).
Byte Arrays (bytearray) - Mutable version of bytes.
Memory Views (memoryview) - Memory-efficient sequence.

2. Difference Between Strings, Lists, and Tuples
Feature 	String (str)	List (list)	            Tuple (tuple)
Mutable?	No	             Yes	                       No
Indexed?    Yes	             Yes	                       Yes
Uses	    Text	       Collection of items	      Immutable collection

3. Explain how indexing works in Python with an example
Indexing is the way to access elements of a sequence (like strings, lists, or tuples) using their position (index).
Starts from 0 (First element → index 0, Second → index 1, etc.).
Negative Indexing: -1 refers to the last element, -2 to the second-last, and so on

-Key Points:
- sorted() sorts the list without modifying the original.
- lambda x: x[1] extracts the second element for sorting.
- The tuples are arranged in increasing order of the second element.


