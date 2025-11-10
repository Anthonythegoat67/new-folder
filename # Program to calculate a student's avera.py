# Program to calculate a student's average and determine approval

# Get exam scores from the user
score_A = float(input("Enter score for Exam A: "))
score_B = float(input("Enter score for Exam B: "))
score_C = float(input("Enter score for Exam C: "))

# Calculate the average
average = (score_A + score_B + score_C) / 3

# Display the average
print(f"\nAverage score: {average:.2f}")

# Determine approval status
if average >= 7:
    print("Status: Approved ✅")
else:
    print("Status: Not approved ❌")
