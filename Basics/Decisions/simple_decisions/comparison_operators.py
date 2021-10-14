# Reading the users input
print("Please enter the first number")
first_num = int(input())

print("Please enter the second number")
second_num = int(input())

# Program decides which number is larger/smaller
if first_num < second_num:
    print("The first number is the smallest.")
elif first_num > second_num:
    print("The second number is the smallest.")
else:
    print("These two numbers are equal")
