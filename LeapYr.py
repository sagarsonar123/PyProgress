#leap year

year=int(input("Please enter a year "))


if (year%4) == 0  :
    if (year%100) ==0:
        if (year%400) == 0:
            print("Year is a leap year")
        else:
            print("Year is not a leap year")
    else:
        print("year is a leap year")
else:
    print("Year is not a leap year")