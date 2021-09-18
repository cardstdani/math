import matplotlib.pyplot as plt

def f(n):
    if (n % 2) == 0:
        return int(n / 2)
    else:
        return ((3 * n) + 1)

x = []
y = []

for i in range(1, 1000):
    x.append(i)
    y.append(f(i))

print(x)
print(y)
plt.plot(x, y)
plt.show()
