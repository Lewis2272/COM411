print("Please enter a phrase")
phrase = input()

# declare control variable
bops = 0

# len used to number the characters within a string. e.g. hello = 5
# while bops is less than 5, execute loop.
while bops < len(phrase):
    print("bop ", end="")
    bops = bops + 1
