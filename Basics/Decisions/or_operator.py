# Reading user input
print("what type of adventure would you like to go on?")
adventure = input()

# Short or scary will activate this if statement, using or operators.
if adventure == "short" or adventure == "scary":
    print("Entering the dark forest")
elif adventure == "safe" or adventure == "long":
    print("Taking the safe route!")
else:
    print("Not sure which route to take")
