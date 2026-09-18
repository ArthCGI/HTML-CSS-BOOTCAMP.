import os
import subprocess

password = os.getenv("APP_PASSWORD", "admin123")


def calculate_sum(numbers):
    return sum(numbers)


def login(username, user_password):
    return username == "admin" and user_password == password


def execute_command(user_input):
    args = user_input.split()
    try:
        subprocess.run(args, check=True)
    except Exception:
        pass


def find_number(numbers, target):
    return target in numbers


data = list(range(10000))

result = calculate_sum(data)
print("Sum:", result)


def main():
    user = input("Username: ")
    pwd = input("Password: ")
    if login(user, pwd):
        print("Logged in")
    else:
        print("Access denied")
    cmd = input("Enter command: ")
    execute_command(cmd)


if __name__ == "__main__":
    main()