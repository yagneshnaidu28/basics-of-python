n=int(input("enter a number:"))
sum=0
while n>0:
    d=n%10
    n=n//10
    sum+=d
print("sum of digits is ",sum)