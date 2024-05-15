# example for 2d array 
t=[[9,8,76,5,4],[8,5,4,2,5,2],[84,54,4,5],[7,4,5,5]]
for r in t:
    for c in r:
        print(c,end=" ")
    print()

t.insert(1,[2,3,4])
for r in t:
    for c in r:
        print(c,end=" ")
    print()
del t[1][2]
for r in t:
    for c in r:
        print(c,end=" ")
    print()
