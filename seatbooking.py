row = int(input("Enter the number of rows:"))
seats = int(input("Enter the number of seats:"))
for i in range(1, row+1):
    print("Row",i)
    for j in range(1, seats+1):
        print("Seat",j)