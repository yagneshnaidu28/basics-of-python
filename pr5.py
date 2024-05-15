#two dimensional array
from array import *
x=[[2,34,5,67],[3,44,1],[65,4,3,9],[9,4,3,2]]
print(x[1][0])
print(x[0])
print(x[1])

print(x)

for i in x:
    for y in i:
        print(y,end=' ')
    print()

print(type(x))

x.insert(2,[3,4,55,6])# to insert value at index in 2d array

for i in x:
    for y in i:
        print(y,end=' ')
    print()


x[1]=[11,3,4,5]# update the value of 2d array
x[0][3]=999
for i in x:
    for y in i:
        print(y,end=' ')
    print()

print("")

del x[2]
for i in x:
    for y in i:
        print(y,end=' ')
    print()
