def fact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n*fact(n-1)
print("---FACTORIAL---")
print(" ")
num = int(input("Enter a number : "))
res = fact(num)
print("The factorial of {} is {} .".format(num,res))