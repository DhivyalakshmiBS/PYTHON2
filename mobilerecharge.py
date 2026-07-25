def recharge(amount):
    if amount == 250:
        print("28 days plan is activated..")
    elif amount == 350:
        print("56 days plan is activated..")
    elif amount == 450:
        print("81 days plan is activated..")
    else:
        print("Enter the correct amount")
amt = int(input("Enter the amount to recharge:"))
recharge(amt)