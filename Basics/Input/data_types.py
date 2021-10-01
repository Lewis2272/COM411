# Calculate and display BMI from user input

# Name of user using string input
print("What is your name human?")
name = str(input())

# Age of user using int input
print("How old are you? (in years)")
age = int(input())

# Height of user using float input
print("How tall are you? (in meters)")
height = float(input())

# Weight of user using int input
print("How much do you weigh? (in kilograms)")
weight = float(input())

# Calculation for BMI
bmi = weight / height**2
print(f"{name} you are {age} years old and your bmi is {bmi}")

