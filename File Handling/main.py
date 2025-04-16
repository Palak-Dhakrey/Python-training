import csv
import os

def process_student_marks():
    students = []
    try:
        with open('students.txt', 'r') as file:
            for line in file:
                name, mark = line.strip().split(',')
                students.append((name, int(mark)))
    except FileNotFoundError:
        print("students.txt file not found.")
        return

    if not students:
        print("No student data found.")
        return

    avg = sum(mark for _, mark in students) / len(students)
    print(f"Average marks (from students.txt): {avg:.2f}")

    with open('top_students.txt', 'w') as file:
        for name, mark in students:
            if mark > avg:
                file.write(f"{name},{mark}\n")

    with open('students.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Grade'])
        writer.writeheader()
        for name, mark in students:
            writer.writerow({'Name': name, 'Grade': mark})

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")

    with open('students.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Grade'])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({'Name': name, 'Age': age, 'Grade': grade})

def view_students():
    try:
        with open('students.csv', 'r') as file:
            reader = csv.DictReader(file)
            print("\n--- Student Records ---")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("students.csv not found.")

def find_above_grade():
    try:
        threshold = float(input("Enter grade threshold: "))
        with open('students.csv', 'r') as file:
            reader = csv.DictReader(file)
            print(f"\n--- Students with grade above {threshold} ---")
            found = False
            for row in reader:
                try:
                    if float(row['Grade']) >= threshold:
                        print(row)
                        found = True
                except ValueError:
                    continue
            if not found:
                print("No students found above the given grade.")
    except FileNotFoundError:
        print("students.csv not found.")
    except ValueError:
        print("Invalid grade input.")

def show_average_grade():
    try:
        with open('students.csv', 'r') as file:
            reader = csv.DictReader(file)
            grades = []
            for row in reader:
                try:
                    grades.append(float(row['Grade']))
                except ValueError:
                    continue
            if grades:
                avg = sum(grades) / len(grades)
                print(f"\nAverage grade: {avg:.2f}")
            else:
                print("No valid grades to calculate average.")
    except FileNotFoundError:
        print("students.csv not found.")

def main():
    process_student_marks()
    while True:
        print("\n--- Student Records Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Find Students Above Grade")
        print("4. Show Average Grade")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            find_above_grade()
        elif choice == '4':
            show_average_grade()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

