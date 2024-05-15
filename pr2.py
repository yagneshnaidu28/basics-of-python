#linear list - sequential order of data 
#stack
#queue
#linear list
# array -fix no.of items and these items should be same type contains element and index
        #operations: traverse -visit every element one by one 
        #insertion,deletion,search,update
from array import *
array1 = array('b',[-1,2,3]) # i is refering to the signed integer #creating 
for x in array1:
    print(x)


print("\n",array1[0])# retrieving the elements
print(array1[1])

array1.insert(0,3)# insert the elements
for x in array1:
    print("array is",x)
array1.remove(2)#deleting the elements 
for x in array1:
    print("array is",x)

print(array1.index(-1))#for search operation it retrieves the index value of given element


array1[1]=4   #update the value of the given index in the array
for x in array1:
    print("array is",x)


