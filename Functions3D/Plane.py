import numpy as np
import matplotlib.pyplot as plt

res = 500
x = np.linspace(-30, 30, res)
y = np.linspace(-30, 30, res)
x, y = np.meshgrid(x, y)
z = x + y

fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
plt.show()
