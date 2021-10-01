print("Welcome! Please enter the name of your robot")
name = str(input())

print(f"Your robots name is {name}\nHow many lives do they have?")
lives = int(input())

print("Please enter their shield level")
shields = int(input())

print("Finally, enter their energy level")
energy = int(input())

print(f"BEHOLD! {name}\nSTAT LEVEL COMING IN AT.. ")
print(f"TOTAL HEALTH: {'❌' * lives}")
print(f"SHIELD LEVELS AT: {'✨' * shields}")
print(f"ENERGY READINGS OVER: {'☕' * energy}")
