
a=int (input("enter the value of a:"))
b=int (input("enter the value of b:"))
c=int (input("enter the value of c:"))

print("your equation is",a,"x**2",b,"x +",c, sep="")

d=(b**2)-(4*a*c)

t=(-b + (d**0.5)) / (2*a)

w=(-b - (d**0.5)) / (2*a)

print("first root is:",t)
print("second root is:",w)
