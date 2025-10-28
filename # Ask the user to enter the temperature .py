# Ask the user to enter the temperature in Fahrenheit
fahrenheit = float(input("Enter the temperature in Fahrenheit (°F): "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9

# Convert Celsius to Kelvin
kelvin = celsius + 273.15

# Display the results
print("\n--- Temperature Conversion ---")
print(f"Fahrenheit: {fahrenheit:.2f} °F")
print(f"Celsius: {celsius:.2f} °C")
print(f"Kelvin: {kelvin:.2f} K")
