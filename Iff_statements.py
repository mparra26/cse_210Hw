# Ask the user for their grade percentage
grade = float(input("Enter your grade percentage: "))

# Determine the letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Print the letter grade
print(f"Your letter grade is: {letter}")

# Pass/fail message
if grade >= 70:
    print("Congratulations! You passed the course.")
else:
    print("Don't worry, keep trying and you'll get it next time!")

    # Ask the user for their grade percentage
grade = float(input("Enter your grade percentage: "))

# Determine the letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Print the letter grade
print(f"Your letter grade is: {letter}")

# Pass/fail message
if grade >= 70:
    print("Congratulations! You passed the course.")
else:
    print("Don't worry, keep trying and you'll get it next time!")