total = 0
while True:
    steps = int(input("Enter the count of the steps:"))
    if steps == 0:
        break
    elif steps<0:
        print("Invalid steps")
        continue
    total += steps
print("Today total step counts:",total)