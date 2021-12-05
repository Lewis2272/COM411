print("What level of brightness is required? (Make it an even number)")

brightness = int(input())

print("Adjusting brightness")
for count in range(2, brightness+1, 2):
    print(f"Beeps brightness level:{'*'*count}")
    print(f"Bops brightness level:{'*'*count}")

print("Adjustments complete!")
