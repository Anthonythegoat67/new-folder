# Program to print the multiplication table of a given number

# Get the number from the user
number = int(input("Enter a number to see its multiplication table: "))

# Print the table header
print(f"\nMultiplication Table for {number}")
print("-" * 30)

# Generate and print the table (from 1 to 10)
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i:2} = {result}")

print("-" * 30)
