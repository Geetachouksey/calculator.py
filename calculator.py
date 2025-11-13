# calculator.py
# A simple Command-Line Calculator App
# Author: Your Name
# Date: 2025-11-13

# --- Function Definitions ---
def add(a, b):
    """Return sum of a and b"""
    return a + b

def subtract(a, b):
    """Return difference of a and b"""
    return a - b

def multiply(a, b):
    """Return product of a and b"""
    return a * b

def divide(a, b):
    """Return division of a by b, handles division by zero"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


# --- Main CLI Application ---
def calculator():
    print("===================================")
    print("     Simple CLI Calculator")
    print("===================================")

    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("\nEnter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("\nThank you for using the calculator. Goodbye! 👋")
            break

        if choice not in ('1', '2', '3', '4'):
            print("\nInvalid input! Please select a valid option (1-5).")
            continue

        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter numeric values only.")
            continue

        if choice == '1':
            result = add(num1, num2)
            op = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            op = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            op = '*'
        elif choice == '4':
            result = divide(num1, num2)
            op = '/'

        print(f"\n✅ Result: {num1} {op} {num2} = {result}")

# --- Run the app ---
if __name__ == "__main__":
    calculator()
