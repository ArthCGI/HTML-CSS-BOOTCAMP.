import getpass
import os
import subprocess


password = os.getenv("APP_PASSWORD", "admin123")


def calculate_sum(numbers):
    return sum(numbers)


def login(username, user_password):
    return username == "admin" and user_password == password


def execute_command(user_input):
    args = user_input.strip().split()
    if not args:
        return
    try:
        subprocess.run(args, check=False)
    except FileNotFoundError:
        print("Command not found")


def find_number(numbers, target):
    return target in numbers


def main():
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


if __name__ == "__main__":
    main()