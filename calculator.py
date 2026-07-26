def calculate(a,b,option):
    if option == 1:
        print("Sum:",a+b)
    elif option == 2:
        print("Difference:",a-b)
    elif option == 3:
        print("Product:",a*b)
    elif option == 4:
        if b == 0:
            print("ZeroDivisionError")
        else:
            print("Quotient:",a/b)
    elif option == 5:
        print("Remainder:",a%b)
    else:
        print("Invalid option")
num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
print("Press 1 for addition.")
print("Press 2 for subtraction.")
print("Press 3 for multiplication.")
print("Press 4 for division.")
print("Press 5 for modulus.")
choice = int(input("Enter the number in which operation to be executed:"))
calculate(num1,num2,choice)