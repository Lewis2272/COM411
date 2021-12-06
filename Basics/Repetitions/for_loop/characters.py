print("What strange markings do you see?")

markings = str(input())
print("Identifying...")

for position in range(0, len(markings), 1):
    print(f"index {position}:", markings[position])

print("Done!")
