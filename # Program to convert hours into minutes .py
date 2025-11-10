# Program to convert hours into minutes and seconds

# Get the number of hours from the user
hours = float(input("Enter the number of hours: "))

# Perform conversions
minutes = hours * 60
seconds = hours * 3600

# Display the results
print(f"\n{hours} hour(s) is equivalent to:")
print(f"{minutes:.2f} minute(s)")
print(f"{seconds:.2f} second(s)")
