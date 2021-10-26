print("How many live cables must I avoid?")
avoid_cables = int(input())

cable_count = 0
# Main take away is use end function to carry on 2 print statements.
while cable_count < avoid_cables:
    print("Avoiding...", end="")
    cable_count = cable_count + 1
    print(f"...Done! {cable_count} live cables avoided.")

print("All live cables have been avoided.")
