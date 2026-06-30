from datetime import datetime
def get_numbers():
    while True:
        try:
            return int(input("Enter first number: ")), int(input("Enter second number: "))
        except ValueError:
            print("Enter valid numbers.")


def save_history(expression):
    with open("history.txt", "a") as f:
        f.write(expression + "\n")

def clear_history():
    choice = input("Are you sure? (y/n): ").lower()
    if choice == "y":
        with open("history.txt", "w") as f:
            pass
        print("History deleted.")
    else:
        print("Operation cancelled.")


def view_history():
    try:
        with open("history.txt") as f:
            lines = f.readlines()

            if not lines:
                print("History is empty.")
                return

            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line}", end="")
    except FileNotFoundError:
        print("No history found.")


def addition():
    num1,num2 = get_numbers()
    result = num1 + num2
    print(f"Result = {result}")
    save_history(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {num1} + {num2} = {result}")


def subtraction():
    num1,num2 = get_numbers()
    result = num1 - num2
    print(f"Result = {result}")
    save_history(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {num1} - {num2} = {result}")


def multiplication():
    num1,num2 = get_numbers()
    result = num1 * num2
    print(f"Result = {result}")
    save_history(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {num1} * {num2} = {result}")

def division():
    while True:
        try:
            num1,num2 = get_numbers()
            result = num1/num2
            print(f"Result = {result}")
            save_history(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {num1} / {num2} = {result}")
            return
        except ZeroDivisionError:
            print("Cannot divide by zero.")


def modulus():
    while True:
        try:
            num1,num2 = get_numbers()
            result = num1%num2
            print(f"Result = {result}")
            save_history(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {num1} % {num2} = {result}")
            return
        except ZeroDivisionError:
            print("Cannot divide by zero.")


def power():
    num1,num2 = get_numbers()
    result = num1 ** num2
    print(f"Result = {result}")
    save_history(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {num1} ^ {num2} = {result}")


def calculator():
    while True:
        print("\n\n===== Calculator =====\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. View History")
        print("8. Clear History")
        print("9. Exit")

        match input("Enter choice: "):
            case "1": addition()
            case "2": subtraction()
            case "3": multiplication()
            case "4": division()
            case "5": modulus()
            case "6": power()
            case "7": view_history()
            case "8": clear_history()
            case "9": 
                print("Thank you for using the calculator!")
                return
            case _: print("Enter valid choice.")
calculator()