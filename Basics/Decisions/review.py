print("Beep is lost and needs help deciding how to get home\n"
      "2 paths are shown, short and scary? or long and safe")
pathway = input()

if pathway == "short" or pathway == "scary":
    print("Beep braves the shortcut and comes across a log cabin\n"
          "A fireplace contains some old wood planks, what will keep beep warm?")
    short_decision = input()
    if short_decision == "fire" or short_decision == "shelter":
        print("Beep gets comfy for the night and walks back home the following morning")
    else:
        print("Beep fails to keep himself safe and succumbs to the forest")

elif pathway == "long" or pathway == "safe":
    print("Beep is sensible and goes the long way home\n"
          "It starts getting dark, does beep sprint home or take his time?")
    long_decision = input()

    print("To shave off more time Beep can take the side ally home or carry on")
    long_decision_2 = input()
    if long_decision == "sprint" and long_decision_2 == "side ally":
        print("Beep gets home in record time!")
    elif long_decision == "take his time" and long_decision_2 == "carry on":
        print("It is late and cold, but Beep finally makes it home!")

else:
    print("I am not familiar with this command")
