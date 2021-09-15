import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative


def f(x, y):
    return x ** 3 + y ** 3


def derivativeX(f, x, y):
    h = 1 / 1000000000
    m = (f(x + h, y) - f(x, y)) / h
    n = f(x, y) - (m * x)
    return (m, n)


def derivativeY(f, x, y):
    h = 1 / 1000000000
    m = (f(x, y + h) - f(x, y)) / h
    n = f(x, y) - (m * y)
    return (m, n)


def plotLineX(m, n, r=30):
    y = [(m * -r) + n, (m * r) + n]
    ax.plot([-r, r], [yValue, yValue], y)
    return


def plotLineY(m, n, r=30):
    y = [(m * -r) + n, (m * r) + n]
    ax.plot([xValue, xValue], [-r, r], y)
    return


res = 500
x = np.linspace(-30, 30, res)
y = np.linspace(-30, 30, res)
x, y = np.meshgrid(x, y)

# Plot function
fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, f(x, y), cmap='viridis', alpha=0.5)

# Plot point and derivative
xValue = 10
yValue = 20
ax.scatter(xValue, yValue, f(xValue, yValue))

resultX = derivativeX(f, xValue, yValue)
resultY = derivativeY(f, xValue, yValue)

plotLineX(resultX[0], resultX[1])
plotLineY(resultY[0], resultY[1])
plt.show()
