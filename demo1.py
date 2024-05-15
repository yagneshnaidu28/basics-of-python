#get unicode for string 
x="Z"
print(ord(x))
print(chr(97-32))
print(chr(97))
print(chr(97+32))
print(chr(32))

#manipulating

s="i loveYOu"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.isspace())

print("completed \n \n \n ")





x="rEd Flower234"
print(x.startswith("rEd"))
print(x.endswith("234"))
print(x.count("l"))
z="do you have an extra pen because my friend needs "
print(z.count("e"))
print(z.find("u"))
print(z.find("love"))
print(z.find("p"))
print(z.index("frie"))
print(z.rfind("o"))
#print(z.lfind("o"))
print(z.rjust(20))
print(z.rjust(5))
print(z.ljust(3))
print(s.center(20,"*"))

s="hello\tworld"
s.expandtabs()
print(s)
print(s.expandtabs(15))




v="***hello mr.peter coolcoolcool***"
print(v.strip("*"))
print(v.strip("cool"))
print(v.rstrip("*"))
print(v.lstrip("*"))
print(v.replace("cool","hot"))
w="illi"
if s == s[::-1]:
    print("palindrome")
else:
    print("not palindrome")