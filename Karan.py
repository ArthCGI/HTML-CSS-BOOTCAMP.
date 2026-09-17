import os
import subprocess
import shlex

# Retrieve password from environment variable; fallback for demonstration purposes
PASSWORD = os.getenv("APP_PASSWORD", "admin123")


def calculate_sum(numbers):
    return sum(numbers)


def login(username, user_password):
    return username == "admin" and user_password == PASSWORD


def execute_command(user_input):
    """Execute a command safely without using a shell."""
    args = shlex.split(user_input)
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
    except FileNotFoundError:
        print("Command not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


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