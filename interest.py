principal_amount = int(input("Enter the principal amount:"))
rate = int(input("Enter the rate amount:"))
time = int(input("Enter years: "))
simple_interest = ( principal_amount * rate * time) / 100
print("Principal Amount :",principal_amount)
print("Rate             :",rate)
print("Time             :",time)
print("Simple Interest  :",simple_interest)
print("Total Amount     :",principal_amount+simple_interest)