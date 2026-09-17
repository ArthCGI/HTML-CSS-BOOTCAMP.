# BAD CODE - DO NOT USE IN PRODUCTION

import os
import shlex

password = os.getenv("CODEREFINE_DEMO_PASSWORD", "")


def calculate_sum(numbers):
    return sum(numbers)


def login(username, user_password):
    return username == "admin" and bool(password) and user_password == password


def execute_command(user_input):
    return shlex.split(user_input)


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
