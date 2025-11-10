# Program to convert feet into various units

# Get the number of feet from the user
feet = float(input("Enter the distance in feet: "))

# Conversion factors
yards = feet / 3              # 1 yard = 3 feet
miles = feet / 5280           # 1 mile = 5280 feet
inches = feet * 12            # 1 foot = 12 inches
leagues = feet / 15840        # 1 league = 3 miles = 15840 feet
meters = feet * 0.3048        # 1 foot = 0.3048 meters

# Display the results
print(f"\n{feet} foot/feet is equivalent to:")
print(f"{yards:.4f} yard(s)")
print(f"{miles:.6f} mile(s)")
print(f"{inches:.2f} inch(es)")
print(f"{leagues:.6f} league(s)")
print(f"{meters:.4f} meter(s)")
