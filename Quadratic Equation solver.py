#The Python Programm to solve Quadratic Equation Solver
import math
a=int(input())
b=int(input())
c=int(input())
#eq=a*x^2+b*x+c
if ((b**2)-(4*a*c))<0:
    print("The roots are imaginary and python cannot compute iota")
else:
    r1=(-1*b+math.sqrt(b**2-4*a*c))/(2*a)
    r2=(-1*b-math.sqrt(b**2-4*a*c))/(2*a)
    print("the roots are ",r1,r2)
