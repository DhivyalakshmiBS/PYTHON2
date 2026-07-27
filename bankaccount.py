def deposit():
    balance = int(input("Enter the balance amount:"))
    amount = int(input("Enter the amount to deposit:"))
    print("Current Balance",balance+amount)
def with_draw():
    balance = int(input("Enter the balance amount:"))
    amount = int(input("Enter the amount to withdraw:"))
    if balance < amount:
        print("Insufficient Balance")
    else:
        print("Current Balance",balance-amount)
def check_balance():
    balance = int(input("Enter the balance amount:"))
    print("Balance Amount:",balance)
def transfer():
    to_acct_num = int(input("Enter the account number to send the amount:"))
    amount = int(input("Enter the amount to be transferred:"))
    print("Money is transferred to:",to_acct_num)
    print("Amount to be transferred:",amount)
print("=========Welcome to XYZ Bank=========.")
print("Press 1 to deposit.")
print("Press 2 to withdraw.")
print("Press 3 to check the balance.")
print("Press 4 to transfer money.")
print("Press 5 to exit.")
choice = int(input("Enter the choice of the operation to perform:"))
if choice == 1:
    deposit()
elif choice == 2:
    with_draw()
elif choice == 3:
    check_balance()
elif choice == 4:
    transfer()
elif choice == 5:
    print("Exit")
else:
    print("Invalid option")