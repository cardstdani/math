import math
from matplotlib import pyplot as plt

xSin = [0]
ySin = [math.sin(0)]

pointsPerUnit = 100
amplitude = 4
initialPhase = math.pi / 2
period = 5
frequency = 1 / period
angularVelocity = (2 * math.pi) / period

maxNumber = period * 4

for i in range(maxNumber * pointsPerUnit):
    xSin.append(xSin[i] + (1 / pointsPerUnit))
    time = xSin[i + 1]
    ySin.append(amplitude * math.sin((angularVelocity * time) + initialPhase))

plt.plot(xSin, ySin)
plt.legend(["Sin"])
plt.grid(color='#1f1f1f', linestyle='-', linewidth=0.1)
plt.show()
