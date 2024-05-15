#stack - lifo 

list1=[]
def push(i):
    list1.append(i)
    
def pop():
    if len(list1) >= 1:
        list1.pop()
        index=-1
    else:
        print('cant delete from empty list')

for i in range(0,4):

    x=int(input("enter for operation \n 1.push \n 2.pop \n  "))

    if(x==1):
        y=int(input('enter no.of elements to be added to stack:'))
        for i in range(0,y):
            item=int(input("enter element to be added"))
            push(item)
    print(list1)

    if(x==2):
        pop()

    print(list1)