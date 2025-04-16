# Task 1: Read and print contents of notes.txt line-by-line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# Task 2: Count the number of lines in poem.txt
with open("poem.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

# Task 3: Write 5 tasks to reminder.txt, one per line
tasks = [
    "Complete Python assignment",
    "Go for a walk",
    "Call mom",
    "Read a book",
    "Prepare dinner"
]

with open("reminder.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

# Task 4: Append a new task to reminder.txt without deleting existing ones
new_task = "Practice coding problems"

with open("reminder.txt", "a") as file:
    file.write(new_task + "\n")

# Task 5: Check if data.txt exists before opening
import os

if os.path.exists("data.txt"):
    with open("data.txt", "r") as file:
        print(file.read())
else:
    print("The file data.txt does not exist.")


