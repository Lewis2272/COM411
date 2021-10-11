# Asking the user which direction to move the paint brush
print("Towards which direction should I paint?")
direction = input()

if direction == 'up':
    print("I am painting in the upward direction")
elif direction == 'down':
    print("I am painting in the downward direction")
elif direction == 'right':
    print("I am painting to the right")
elif direction == 'left':
    print("I am painting to the left")
else:
    print("I am unsure of this direction")
