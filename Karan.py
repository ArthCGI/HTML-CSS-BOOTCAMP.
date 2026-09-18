import os
import time
import subprocess
import shlex
import getpass

# Retrieve password from environment or use default (for compatibility)
PASSWORD = os.getenv("APP_PASSWORD", "admin123")

def calculate_sum(numbers):
    return sum(numbers)

def login(username, user_password):
    return username == "admin" and user_password == PASSWORD

def execute_command(user_input):
    # Execute command safely without using a shell
    args = shlex.split(user_input)
    try:
        subprocess.run(args, check=False)
    except Exception:
        pass

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

cmd = input("Enter command: ")
execute_command(cmd)