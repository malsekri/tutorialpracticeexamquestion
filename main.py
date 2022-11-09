name = input("What is your name?")
a = int(input("What is the value of a?"))
b = int(input("What is the value of b?"))
c = int(input("What is the value of c?"))
d = int(input("What is the value of d?"))

e = ((-b**3/(27*a**3))+((b*c)/(6*a**2))-(d/2*a))
f = ((c/3*a)-((b**2)/(9*a**2)))**3
g = -(b/3*a)
m = ((e**2)+f)**0.5

y = (e+m)**(1/3)
z = (e-m)**(1/3)

def f(y,z,g):
    x = y+z+g
    return(x.real)

print("Hello", name, "the answer to the equation is",f(y,z,g))

quit()
