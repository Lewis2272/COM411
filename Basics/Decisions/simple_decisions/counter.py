# Reading users input
print("Please enter the first whole number.")
first_num = int(input())

print("Please enter the second whole number.")
second_num = int(input())

print("Please enter the third whole number.")
third_num = int(input())

# Declare total number of odd and even numbers
odd = 0
even =0

# If a number can be divided by 2 = add 1 to even, if not add 1 to odd
if first_num % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
if second_num % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
if third_num % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

# Print result including odd/even variables.
print(f"There were {even} even and {odd} odd numbers.")