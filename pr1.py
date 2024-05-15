def square(s):
    a=s*s
    return a
def rectangle(l,b):
    a=l*b
    return a
def circle(r):
    a=2*3.1416*r*r
    return a
def triangle(b,h):
    a=0.5*b*h
    return a
for i in range(0,10):
    x=int(input(" \n 1. for area of square \n 2.for area of rectangle \n 3. for area of circle \n 4. for area of triangle \n enter:"))

    if(x==1):
        side=float(input("enter side of square (incms):"))
        print("area of square is",square(side))
    if(x==2):
        length=float(input("enter length of rectangle \n"))
        breadth=float(input("enter breadth of rectangle \n"))
        print("area of rectangle is",rectangle(length,breadth))
    if(x==3):
        radius=float(input("enter radius of circle: "))
        print("area of circle is",circle(radius))
    if(x==4):
        base=float(input("enter base of triangle "))
        height=float(input("enter height of triangle"))
        print("area of triangle is",triangle(base,height))
    if(x>4):
        print("choose only area for square,rectangle,triangle,don't enter more than 4, enter only from 1 to 4")
        i=i-1