n=int(input("enter a number"))
if(n%5==0 and n%7==0):
    print("fizzbuzz")
elif(n%7==0):
    print("buzz")
elif(n%5==0):
    print("fizz")
else:
    print("number not divisible by either 7 or 5")