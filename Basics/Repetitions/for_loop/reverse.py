print("What phrase do you see?")
phrase = str(input())

print("Reversing...")
print("The phrase is ", end="")

for reverse in range(len(phrase)-1, -1, -1):
    print(phrase[reverse], end="")
