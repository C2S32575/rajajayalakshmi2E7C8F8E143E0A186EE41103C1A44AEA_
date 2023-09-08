def leapyear(y):
  if (y%4==0 and y%100!=0) or y%400==0:
    print("{} is leap year.".format(y))
  else:
    print("{} is not a leap year.".format(y))
print("---LEAP YEAR---")
print(" ")
y = int(input("Enter a year : "))
leapyear(y)
