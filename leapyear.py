year=int(input("enter year:"))
rem=year%4
if rem==0:
    if year%100==0:
        if year%400==0:
            print("yes this year is a leap year")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
else:
    print("this year is not a leap year")
