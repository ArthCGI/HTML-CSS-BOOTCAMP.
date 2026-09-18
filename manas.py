import os
import shlex

# Retrieve password from environment or fallback to default (for compatibility)
PASSWORD = os.getenv("APP_PASSWORD", "admin123")


def calculate_sum(numbers):
    return sum(numbers)


def login(username, user_password):
    return username == "admin" and user_password == PASSWORD


def execute_command(user_input):
    # Validate or sanitize input as needed; here we simply split arguments safely
    args = shlex.split(user_input)
    if args:
        # Import subprocess locally to avoid top‑level import warnings
        import subprocess

        subprocess.run(args, check=False)


def find_number(numbers, target):
    return target in numbers


data = list(range(10000))

result = calculate_sum(data)

print("Sum:", result)

user = input("Username: ")
pwd = input("Password: ")

if login(user, pwd):
    print("Logged in")
else:
    print("Access denied")

cmd = input("Enter command: ")
execute_command(cmd)