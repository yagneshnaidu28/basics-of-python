#string operations
x="yagnesh"
y="naidu"
#length of string
print(len(x))
#concatenation 
print(x+y)

z="cherry"
print(z+z)
print(z*3)


#indexing
s="python class"
print(s[4])
print(s[-1])
print(s[-4])
print(s[len(s)-2])



#slicing
print(s[7:13])
print(s[1:12:2])
print(s[11:3:-1])
print(s[::-1])


#membership operator

x="d"
name="harsha"
if x in name:
    print("yes")
s="c"
if s not in name:
    print("no")

a="i study js"
print(a[8])
print(j=a[8])
