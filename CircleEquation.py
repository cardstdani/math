point = [1, 2]
radius = 3

equation = "(x - " + str(point[0]) + ")²" + " + (y - " + str(point[1]) + ")² = " + str(radius * radius)
fullEquation = "x² " + str(-2 * point[0]) + "x + y² + " + str(-2 * point[1]) + "y + " + str(
    (point[0] * point[0]) + (point[1] * point[1])) + " = " + str(radius * radius)

print(equation)
print(fullEquation)
