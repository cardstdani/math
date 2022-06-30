import numpy as np
import matplotlib.pyplot as plt
import math, ast
from sympy import *

dx = symbols('x')
f = lambda x : cos(x)

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

def nderivative(func, i):
    return eval("func" + ".diff(dx)"*i)

s = "lambda x, a : f(a) + " + " + ".join([f"nderivative(f(dx), {i}).doit().subs("+"{dx:a}"+f")*((x-a)**{i})*(1/factorial({i}))" for i in range(1, 19)])
p = eval(s)
print(s)

x = np.linspace(-15, 15, 100)
y = [f(i) for i in x]

y2 = [p(i, 0) for i in x]

plt.plot(x, y)
plt.plot(x, y2)
plt.ylim([-4, 4])
plt.show()
