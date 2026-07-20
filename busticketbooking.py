seat = int(input("Enter the seat number for reservation:"))
if seat == 0:
    print("Booking closed")
elif (1 > seat or seat > 20):
    print("Invalid seat number.")
else:
    print("Seat Booked.")