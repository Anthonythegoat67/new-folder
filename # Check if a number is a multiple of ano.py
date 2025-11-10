# Check if a number is a multiple of another

# Get user input
a = float(input("Enter number a: "))
b = float(input("Enter number b: "))

# Check for division by zero
if b == 0:
    print("Error! Division by zero is not allowed.")
else:
    # Check if a is a multiple of b
    if a % b == 0:
        factor = a / b
        print(f"{a} is a multiple of {b} by a factor of {int(factor)}.")
    else:
        print(f"{a} is not a multiple of {b}.")
