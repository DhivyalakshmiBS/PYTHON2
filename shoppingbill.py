bill = int(input("Enter the amount of bill:"))
while True:
    choice = input("Whether you want to add items(Y) or (N):")
    if(choice == "Y"):
        amount = int(input("Enter the amount:"))
        bill += amount
    else:
        break
    while(bill >= 5000):
        print("Limit exceeded")
        break
    print("Total amount:",bill)
    
        