# Task 1: Remove blank lines from input.txt and write to cleaned.txt
with open("input.txt", "r") as infile, open("cleaned.txt", "w") as outfile:
    for line in infile:
        if line.strip(): 
            outfile.write(line)

# Task 2: Replace "Python" with "PYTHON" in article.txt
with open("article.txt", "r") as file:
    content = file.read()

updated_content = content.replace("Python", "PYTHON")

with open("article.txt", "w") as file:
    file.write(updated_content)

# Task 3: Convert contents of input.txt to uppercase and write to output.txt
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())

# Task 4: Generate pass/fail report from students.txt
with open("students.txt", "r") as infile, open("report.txt", "w") as outfile:
    for line in infile:
        name, marks = line.strip().split(",")
        status = "Pass" if int(marks) >= 50 else "Fail"
        outfile.write(f"{name},{marks},{status}\n")

# Task 5: Reverse the lines in quotes.txt and write to reversed_quotes.txt
with open("quotes.txt", "r") as infile:
    lines = infile.readlines()

with open("reversed_quotes.txt", "w") as outfile:
    for line in reversed(lines):
        outfile.write(line)

