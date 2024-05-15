list1=[35,54,84,54,57,43]
target=54
print(list1.index(target))
print(list1.count(54))
print(sum(list1))
print(max(list1))
print(min(list1))
r=list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)

#list comprehension

r=[]
for i in range (len(list1)):
    x=list1[i]*list1[i]
    r.append(x)
print(r)

r=[x*x for x in list1]# this is list comprehension technique doing all code in one line
print(r)

list2=[1,2,3,4,5]
s=[y*100 for y in list2 if(y%2==0)]
print(s,"sdsdf")
q=[]
for j in range(len(list2)):
    if(j%2==0):
         n=j*100
         q.append(n)
    print(q)