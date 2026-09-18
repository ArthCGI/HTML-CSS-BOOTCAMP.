import os
import subprocess
import getpass

# Retrieve password from environment variable for authentication
PASSWORD = os.getenv("APP_PASSWORD", "admin123")  # fallback for demonstration only


def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def login(username, user_password):
    return username == "admin" and user_password == PASSWORD


def execute_command(user_input):
    # Split the input into arguments safely
    args = user_input.strip().split()
    if not args:
        return
    try:
        subprocess.run(args, check=False, capture_output=False, text=True)
    except FileNotFoundError:
        print(f"Command not found: {args[0]}")
    except OSError as e:
        print(f"Error executing command: {e}")


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