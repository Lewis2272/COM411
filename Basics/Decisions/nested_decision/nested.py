# Reading users inputs
print("What type of cover does the book have? hard or soft?")
book = input()

# Decide to activate nested decision or not
if book == "soft":
    print("Is the book perfect bound?")
    bound = input()

    # Nested decision activated if met with proper condition
    if bound == "Yes":
        print("Soft cover, perfect bound books are very popular.")
    else:
        print("Soft covers with coils or stitches are great for short books.")

# If condition isn't met then run this instead
else:
    print("Books with hard covers can be more expensive")
