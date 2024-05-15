n=int(input("enter a number"))
for i in range(1,n+1):


    if(n%i==0):
        print(n,"is a prime number")
    else:
        print(n,"is a composite number")