import matplotlib.pyplot as plt
import numpy as np
import math

f = lambda a : [(1+math.cos(i*(2*math.pi/60))**2)**0.5 for i in a]

x = []
y = []

for i in range(1, 400):
  x.append(i)
  l1, l2 = 0, i

  prec = 60000
  width = (l2-l1)/prec
  x1 = [i*width + (width/2) for i in range(prec)]
  y1 = f(x1)

  auc = sum(y1)*width
  y.append(auc)

plt.figure(figsize=(20, 20))
plt.plot(x, y)
