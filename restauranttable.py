table = int(input("Enter the number of tables:"))
chair = int(input("Enter the number of chairs:"))
for i in range(1, table+1):
    print("Table",i)
    for j in range(1, chair+1):
        print("Chair",j)