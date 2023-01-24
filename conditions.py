a = 33
b = 200
if b > a:
    print("b is greater than a")

#Elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#else
a = 50
b = 15
if b > a:
    print("b greater than a")
else:
    print("a greater than b")

#short hand if or else
a = 2
b = 33
print("A") if a > b else print("B")