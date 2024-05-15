# wap to take input of student roll number and marks of three subjects and display them in matrix
t=[[],[],[],[]]
z=int(input("enter no.of students marks should be entered:"))
for i in range(0,z):

    n=input("enter student roll number:")
    f1=int(input("enter marks of first subject:"))
    f2=int(input("enter marks of second subject:"))
    f3=int(input("enter marks of third subject:"))
    t.insert(0,[n,f1,f2,f3])
    

for r in t:
    for c in r:
        print(c,end=" ")
    print()