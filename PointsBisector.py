point1 = [2, 5]
point2 = [4, -7]

middlePoint = [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]
bisectorLine = str(-2 * point1[0] - (-2 * point2[0])) + "x + " + str(-2 * point1[1] - (-2 * point2[1])) + "y + " + str((
            (point1[0] * point1[0]) + (point1[1] * point1[1])) - ((point2[0] * point2[0]) + (point2[1] * point2[1])))

print("M(" + str(middlePoint[0]) + ", " + str(middlePoint[1]) + ")")
print(bisectorLine)
