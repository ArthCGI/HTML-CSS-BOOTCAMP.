import os
import sys
import subprocess

# Load password from environment variable or use default (for demonstration purposes)
PASSWORD = os.getenv("APP_PASSWORD", "admin123")


def calculate_sum(numbers):
    return sum(numbers)


def login(username, user_password):
    return username == "admin" and user_password == PASSWORD


def execute_command(user_input):
    # Split the input into arguments to avoid shell injection
    args = user_input.strip().split()
    if not args:
        return
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}", file=sys.stderr)


def find_number(numbers, target):
    return target in numbers


# Efficient data creation
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