num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
if num1 == num2 == num3:
    print("The numbers are equal")
elif num1 > num2 and num1 > num3:
    print(f"The number {num1} is largest")
elif num2 > num3:
    print(f"The number {num2} is largest")
else:
    print(f"The number {num3} is largest")