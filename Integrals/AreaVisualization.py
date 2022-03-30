import matplotlib.pyplot as plt
import numpy as np
import math

l1, l2 = 0, 40
f = lambda a : [(1+math.cos(i*(2*math.pi/60))**2)**0.5 for i in a]
x = np.linspace(l1, l2)
y = f(x)

prec = 6000
width = (l2-l1)/prec
x1 = [i*width + (width/2) for i in range(prec)]
y1 = f(x1)

auc = sum(y1)*width
print(auc)

plt.plot(x, y)
plt.bar(x1, y1, width=width, color="#01ff09")
