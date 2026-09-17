import getpass
import logging
import os
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_sum(numbers):
    return sum(numbers)

def login(username, user_password):
    expected_password = os.getenv("APP_PASSWORD", "admin123")
    return username == "admin" and user_password == expected_password

def execute_command(user_input):
    args = user_input.split()
    try:
        subprocess.run(args, check=False)
    except subprocess.SubprocessError as e:
        logger.error("Failed to execute command: %s", e)

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