import math

# r = (Ax + By + C = 0)
a = 3
b = 4
c = 0

# P(u, v)
u = 2
v = -1

def distance(a, b, c, u, v):
    return abs(((a * u) + (b * v) + c) / math.sqrt((a * a) + (b * b)))

print(distance(a, b, c, u, v))
