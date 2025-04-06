# 3. Password Strength Checker
 # Classify passwords as "Weak", "Medium", or "Strong" based on length, numbers, uppercase/lowercase letters, and special characters.
 # Loop until a "Strong" password is entered.

import re
def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = not re.search(r"\d", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    special_char_error = not re.search(r"[@$!%*?&#]", password)
    
    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    strength = "Weak"
    
    if sum(errors) == 0:
        strength = "Strong"
    elif sum(errors) <= 2:
        strength = "Medium"
    
    return strength

while True:
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")
    if strength == "Strong":
        break

# 1. Employee Attendance Tracker
# Implement a system that tracks employee attendance.
# Use loops to process multiple employees and conditionals to check attendance.
# Mark employees as "Needs Attention" if absent for more than 3 consecutive days.
import uuid

class Employee:
    def __init__(self, name, age):
        self.id = str(uuid.uuid4())[:8]  
        self.name = name
        self.age = age
        self.attendance = self.get_attendance()

    def get_attendance(self):
        print(f"Enter attendance for {self.name} for the last 7 days (P/A):")
        return [input(f"Day {i+1}: ").strip().upper() for i in range(7)]

    def modify_attendance(self, day, status):
        if 1 <= day <= 7:  # User inputs days from 1 to 7
            self.attendance[day - 1] = status  # Convert to 0-based index
            print(f"Attendance updated for Day {day}.")
        else:
            print("Invalid day selection. Choose from last 7 days (1-7).")

    def check_needs_attention(self):
        for i in range(5):  # Ensure the 3-day sequence is within range
            if self.attendance[i:i+3] == ["A", "A", "A"]:
                return True
        return False

    def view_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}")
        print(f"Attendance (Last 7 days): {' '.join(self.attendance)}")
        print("Status: Needs Attention" if self.check_needs_attention() else "Status: OK")


class AttendanceTracker:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, age):
        emp = Employee(name, age)
        self.employees[emp.id] = emp
        print(f"Employee {name} added with ID: {emp.id}")

    def view_employee(self, emp_id):
        if emp_id in self.employees:
            self.employees[emp_id].view_details()
        else:
            print("Employee not found!")

    def modify_attendance(self, emp_id, day, status):
        if emp_id in self.employees:
            self.employees[emp_id].modify_attendance(day, status)
        else:
            print("Employee not found!")

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted.")
        else:
            print("Employee not found!")

 
def main():
    tracker = AttendanceTracker()
    
    while True:
        print("\nOptions: \n1. Add Employee \n2. View Employee \n3. Modify Attendance \n4. Delete Employee \n5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter Employee Name: ")
            age = input("Enter Employee Age: ")
            tracker.add_employee(name, age)

        elif choice == "2":
            emp_id = input("Enter Employee ID to view details: ")
            tracker.view_employee(emp_id)

        elif choice == "3":
            emp_id = input("Enter Employee ID: ")
            if emp_id in tracker.employees:
                day = int(input("Enter day index (1-7): "))  # User inputs from 1-7
                status = input("Enter status (P/A): ").strip().upper()
                tracker.modify_attendance(emp_id, day, status)
            else:
                print("Employee not found!")

        elif choice == "4":
            emp_id = input("Enter Employee ID to delete: ")
            tracker.delete_employee(emp_id)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

# Banking System with ATM Functionality
#Simulate an ATM system for checking balance, withdrawal, and deposit.
#Use loops for multiple transactions and conditionals to prevent overdraft.
def atm():
    balance = 1000  
    pin = "1234"   
    print("Welcome to Simple ATM")
    user_pin = input("Enter your 4-digit PIN: ")

    if user_pin != pin:
        print("Incorrect PIN. Exiting.")
        return

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"Your current balance is: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount} deposited. New balance: ₹{balance}")
            else:
                print("Invalid deposit amount.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount > balance:
                print("Insufficient balance.")
            elif amount <= 0:
                print("Invalid withdrawal amount.")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn. New balance: ₹{balance}")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 to 4.")
atm()

#Problem 6:Bank Loan Eligibility System
#Create a program to check if a user is eligible for a bank loan based on salary, age, and credit score using nested conditionals.
#Bank Loan Eligibility Checker

print("Welcome to the Loan Eligibility Checker\n")
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary (₹): "))
credit_score = int(input("Enter your credit score (out of 900): "))
if age >= 21:
    if salary >= 25000:
        if credit_score >= 650:
            print("\nYou are eligible for a loan.")
        else:
            print("\nSorry, your credit score is too low.")
    else:
        print("\nSorry, your salary is below the required amount.")
else:
    print("\nSorry, you must be at least 21 years old to apply for a loan.")

#Problem 7: AI Chatbot with Conditional Responses
#Design a simple chatbot that responds differently based on user input (e.g., greetings, questions, or farewell messages).
#Simple AI Chatbot

print("Chatbot: Hello! I'm ChatBot. Type something to talk to me.")
print("Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hey there! How can I help you?")
    
    elif "how are you" in user_input:
        print("Chatbot: I'm just code, but I'm running fine!")

    elif "your name" in user_input:
        print("Chatbot: You can call me ChatBot.")

    elif "bye" in user_input or "exit" in user_input:
        print("Chatbot: Goodbye! Have a nice day :)")
        break

    elif "help" in user_input:
        print("Chatbot: I'm here to chat with you. Ask me anything!")

    else:
        print("Chatbot: Hmm... I didn't understand that. Try saying something else.")

#Problem 8:Traffic Light Simulation
#Simulate a traffic light system using conditionals and loops.
import time

# Simple Traffic Light Simulation

lights = ["Red", "Green", "Yellow"]

print("Traffic Light Simulation Started\n")

for i in range(3):  
    for light in lights:
        if light == "Red":
            print("RED light - Stop")
            time.sleep(2)
        elif light == "Green":
            print("GREEN light - Go")
            time.sleep(2)
        elif light == "Yellow":
            print("YELLOW light - Wait")
            time.sleep(1)
        print() 

print("Simulation Ended")

#Problem 9: Smart Home Automation
#Implement a conditional-based smart home system where temperature, humidity, and motion sensors determine actions (e.g., turning lights and fans on/off).
#Simple Smart Home Automation System

print("Welcome to Smart Home System\n")
temperature = float(input("Enter current temperature (°C): "))
humidity = float(input("Enter current humidity (%): "))
motion = input("Is there motion detected? (yes/no): ").lower()
if temperature > 30:
    print("Action: It's hot! Turning on the fan.")
else:
    print("Action: Temperature is fine. Fan stays off.")

if humidity > 70:
    print("Action: Humidity is high! Turning on dehumidifier.")
else:
    print("Action: Humidity is normal. Dehumidifier stays off.")

if motion == "yes":
    print("Action: Motion detected! Turning on the lights.")
else:
    print("Action: No motion. Lights stay off.")

#Problem 10: Stock Market Trend Analysis
#Write a program to analyze stock prices and predict buy/sell signals based on historical trends using conditionals.
# Simple Stock Market Trend Analyzer

print("Stock Market Trend Analysis\n")
price_day1 = float(input("Enter price 3 days ago: ₹"))
price_day2 = float(input("Enter price 2 days ago: ₹"))
price_day3 = float(input("Enter price 1 day ago: ₹"))
if price_day1 < price_day2 < price_day3:
    print("\nTrend: Price is rising.")
    print("Signal: Consider SELLING to take profit.")
elif price_day1 > price_day2 > price_day3:
    print("\nTrend: Price is falling.")
    print("Signal: Consider BUYING at a lower price.")
else:
    print("\nTrend: Fluctuating or stable.")
    print("Signal: HOLD and wait for a clearer trend.")



