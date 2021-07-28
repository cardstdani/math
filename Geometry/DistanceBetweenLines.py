import math

# r = (Ax + By + C = 0)
a1 = 1
b1 = 3
c1 = -5

# s = (A'x + B'y + C' = 0)
a2 = 1
b2 = 3
c2 = 18

def distance(a1, b1, c1, a2, b2, c2):
    if ((a1 == a2) and (b1 == b2) and (c1 == c2)):
        return 0
    elif ((a1 == a2) and (b1 == b2)):
        divisor = math.sqrt((a1 * a1) + (b1 * b1))
        if (divisor == 0):
            return abs(c2 - c1)
        return abs((c1 - c2) / divisor)
    else:
        return 0

print(distance(a1, b1, c1, a2, b2, c2))
