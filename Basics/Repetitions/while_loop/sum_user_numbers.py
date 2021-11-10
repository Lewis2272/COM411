print("How many numbers should I sum up?")
control_number = 0
user_number = int(input())
total = 0

while control_number < user_number:
    print(f"Please enter number {control_number} of {user_number}:")
    number = int(input())
    total = total + number
    control_number = control_number + 1

print(f"The answer is {total}.")
