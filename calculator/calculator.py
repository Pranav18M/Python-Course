# Simple Calculator With History
# Author: Pranav

HISTORY_FILE = "history.txt"


def save_history(record):
    with open(HISTORY_FILE, "a") as file:
        file.write(record + "\n")


def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            data = file.read()
            if data == "":
                print("\nNo history found.")
            else:
                print("\n----- Calculation History -----")
                print(data)
    except FileNotFoundError:
        print("\nNo history file found.")


def clear_history():
    open(HISTORY_FILE, "w").close()
    print("\nHistory cleared successfully.")


def get_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input! Enter numbers only.")
        return None, None


def add():
    a, b = get_numbers()
    if a is not None:
        result = a + b
        record = f"{a} + {b} = {result}"
        print("Result:", result)
        save_history(record)


def subtract():
    a, b = get_numbers()
    if a is not None:
        result = a - b
        record = f"{a} - {b} = {result}"
        print("Result:", result)
        save_history(record)


def multiply():
    a, b = get_numbers()
    if a is not None:
        result = a * b
        record = f"{a} * {b} = {result}"
        print("Result:", result)
        save_history(record)


def divide():
    a, b = get_numbers()
    if a is not None:
        if b == 0:
            print("Cannot divide by zero!")
        else:
            result = a / b
            record = f"{a} / {b} = {result}"
            print("Result:", result)
            save_history(record)


def main():
    while True:
        print("\n===== SIMPLE CALCULATOR =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Clear History")
        print("7. Exit")

        choice = input("Choose option (1-7): ")

        if choice == "1":
            add()
        elif choice == "2":
            subtract()
        elif choice == "3":
            multiply()
        elif choice == "4":
            divide()
        elif choice == "5":
            show_history()
        elif choice == "6":
            clear_history()
        elif choice == "7":
            print("Exiting Calculator...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
