print("Calculating the sum of the first 100 numbers...")
# Control Variable
number = 1

total = 0

# Total is added to number, whilst number carries on adding sequentially +1+2+3
while number <= 100:
    total = total + number
    number = number + 1

print(f"...Done! The answer is {total}")