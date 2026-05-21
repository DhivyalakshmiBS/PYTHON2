score=int(input("Enter the score: "))
if score>=90:
    print("Assigned Grade:A")
elif score>=80 and score<90:
    print("Assigned Grade:B")
elif score>=70 and score<80:
    print("Assigned Grade:C")
elif score>=60 and score<70:
    print("Assigned Grade:D")
else:
    print("Assigned Grade:F")