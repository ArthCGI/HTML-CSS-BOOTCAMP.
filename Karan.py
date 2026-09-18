import os
import subprocess
import getpass

# Retrieve password from environment variable; fallback to a default for demonstration purposes
PASSWORD = os.getenv("APP_PASSWORD", "admin123")

def calculate_sum(numbers):
    return sum(numbers)

def login(username, user_password):
    return username == "admin" and user_password == PASSWORD

def execute_command(user_input):
    # Execute command without using the shell to avoid injection risks
    subprocess.run(user_input, shell=False, check=False)

def find_number(numbers, target):
    return target in numbers

data = list(range(10000))

result = calculate_sum(data)

print("Sum:", result)

user = input("Username: ")
pwd = getpass.getpass("Password: ")

if login(user, pwd):
    print("Logged in")
else:
    print("Access denied")

cmd = input("Enter command: ").split()
execute_command(cmd)