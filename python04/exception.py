#!/usr/bin/env python3

# Divide two numbers
def div(a, b):
    return a / b

# Method 1: prevent the exception
def safe_division_prevent():
    print("\n--- Method 1: Prevent the exception ---")
    while True:
        try:
            a = int(input("a = "))
            b = int(input("b = "))
            if b == 0:
                print("b is zero. Division by zero is not allowed. Try again.")
                continue
            print("Result:", div(a, b))
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")

# Method 2: handle the exception
def safe_division_handle():
    print("\n--- Method 2: Handle the exception ---")
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        print("Result:", div(a, b))
    except ValueError:
        print("Invalid input. Please enter integers only.")
    except ZeroDivisionError:
        print("Division by zero occurred and was handled safely.")
    print("Program continues after exception handling.")

# Main program
def main():
    print("Division Example: Preventing and Handling Exceptions")
    safe_division_prevent()
    safe_division_handle()

if __name__ == "__main__":
    main()
