list1=[19,54,62,54]
print(list1[::-1])
print(list1*3)
list2=[1,2,4,5]
print(list1+list2)


for i in range (len(list1)):
    print(list1[i]+10)
for i in list1:
    print(i+1)
for i,x in enumerate(list1):
    print(i,x)
i=0
n=len(list1)
while i<n:
    print(list1[i]+12)
    i+=1