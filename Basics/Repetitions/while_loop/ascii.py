print("How many bar should be charged?")
charged_bars = int(input())

bars_count = 0
while bars_count < charged_bars:
    bars_count = bars_count + 1
    print(f"Charging: {'' * bars_count}")

print("The battery ss fully charged")
