import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation 

x = np.linspace(-40, 40, 500)
y = []

#Function to evaluate
def f(n):
  return n**3

def derivative(f, x):
  h = 1 / 1000000000
  m = (f(x+h) - f(x)) / h
  n = f(x) - (m*x)
  return (m, n)

def plotLine(m, n, r=20):
  x = [plt.axis()[0], plt.axis()[1]]
  y = [(m*plt.axis()[0]) + n, (m*plt.axis()[1]) + n]
  plt.figure(1)
  plt.plot(x, y)
  return

#Plot function
for i in x:
  y.append(f(i))

plt.figure(1, figsize=(16, 16))
plt.plot(x, y)

#Plot point and derivative
xValue = 30
result = derivative(f, xValue)
plt.scatter(xValue, f(xValue))
plotLine(result[0], result[1])
