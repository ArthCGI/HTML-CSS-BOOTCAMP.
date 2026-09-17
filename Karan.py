import getpass
import os
import shlex


def _get_stored_password() -> str:
    """Retrieve the stored password from environment variables."""
    return os.getenv("CODEREFINE_DEMO_PASSWORD", "")


def calculate_sum(numbers):
    return sum(numbers)


def login(username: str, user_password: str) -> bool:
    stored_password = _get_stored_password()
    return username == "admin" and bool(stored_password) and user_password == stored_password


def execute_command(user_input: str):
    """Parse the command safely without executing it."""
    return shlex.split(user_input)


def main():
    data = range(10_000)

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