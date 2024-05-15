from array import *
array2 = array('i',[9,8,7,45,6,12,3,44])
for i in array2:
    print(i)
array2.insert(3,45)


array2.remove(44)
for i in array2:
    print("adfsf",i)

print(array2.index(6))