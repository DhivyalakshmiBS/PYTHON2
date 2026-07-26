def result(mark):
    if mark < 0 or mark > 100:
        print("Invalid Marks")
    elif mark > 90:
         print("Grade:A")
    elif 80 < mark <=90:
        print("Grade:B")
    elif 70 < mark <=80:
        print("Grade:C")
    elif 60 < mark <=70:
        print("Grade:D")
    else:
        print("Grade:E")
num = int(input("Enter the mark for maths subject:"))
result(num)