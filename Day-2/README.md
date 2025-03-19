KEYPOINTS:
The function does not handle invalid input types (e.g., '10%' as a string).
No error handling for cases where discount is not a valid number.
If discount is negative or greater than 100, it does not check for valid discount ranges.

RACE CONDITION:-A race condition occurs when multiple threads or processes access and modify shared data at the same time, leading to unpredictable results
USE OF LOCK-
lock = threading.Lock(): Creates a lock object.
with lock:: Ensures that only one thread can execute the critical section (counter += 1) at a time.
Other threads must wait for the lock to be released before modifying counter.

Why Do We Use Breakpoints?
A breakpoint is a debugging tool that lets you pause code execution at a specific line to inspect variables, step through code, and find errors.
- Quickly find and fix bugs
- Inspect variable values without print()
- Step through execution line by line
- Debug loops and conditions easily
- Save time by avoiding unnecessary code changes

USE OF YIELD(GENERATOR)
The yield keyword is used in generators, which are special functions that return values one at a time instead of all at once. This helps save memory and improves performance
Generates values one by one
Execution:Pauses execution and resumes later
Performance:Faster and memory-efficient
Iteration:Can be used in a loop (for or next())

USE OF PASS:
The pass statement in Python is used when you need a placeholder for an empty block of code. It allows the program to run without errors while keeping the syntax valid.
