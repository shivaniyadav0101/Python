#we use quadratic equation is ax**2+bx+c
import math
a=int(input("enter your first no"))
b=int(input("enter your second no"))
c=int(input("enter your third no"))
d=math.sqrt(b**2-4*a*c)
root1=-(b+d)/2
root2=-(b-d)/2
print("roots of this equation are:",root1,"and",root2)
