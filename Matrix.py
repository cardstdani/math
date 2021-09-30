class matrix():
    def __init__(self, m=None):
        self.m = m

    def change(self, row, column, newValue):
        self.m[row][column] = newValue

    def setMatrix(self, newMatrix):
        self.m = newMatrix

    def transposed(self):
        n = []
        for j in range(len(self.m[0])):
            n.append([])
            for i in range(len(self.m)):
                n[j].append(self.m[i][j])
        self.setMatrix(n)
        return self

    def __add__(self, n):
        if len(self.m) == len(n.m) and len(self.m[0]) == len(n.m[0]):
            # Sum
            for i in range(len(self.m)):
                for j in range(len(self.m[i])):
                    n.change(i, j, n.m[i][j] + self.m[i][j])
        return n

    def __sub__(self, n):
        if len(self.m) == len(n.m) and len(self.m[0]) == len(n.m[0]):
            for i in range(len(self.m)):
                for j in range(len(self.m[i])):
                    n.change(i, j, self.m[i][j] - n.m[i][j])
        return n

    def __rmul__(self, n):
        # Scalar by matrix multiplication
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                self.change(i, j, self.m[i][j] * n)
        return self

    def __mul__(self, n):
        # Matrix multiplication
        if (len(self.m[0]) == len(n.m)):
            o = []
            for i in range(len(self.m)):
                o.append([])
                for j in range(len(n.m[0])):
                    o[i].append(self.getRowByColumn(i, j, n))
            self.setMatrix(o)
            return self

    def __pow__(self, n):
        # Matrix pow
        n = int((n ** 2) ** (1 / 2))
        s = matrix(self.m)
        for i in range(n - 1):
            self *= s
        return self

    def getRowByColumn(self, row, column, n):
        r = 0
        for i in range(len(self.m[row])):
            r += self.m[row][i] * n.m[i][column]
        return r

    def subDet(self, x, y):
        n = []
        for i in range(len(self.m)):
            if x != i:
                n.append([])
                for a in range(len(self.m[i])):
                    if x != i and y != a:
                        n[len(n) - 1].append(self.m[i][a])
        nm = matrix(n)
        return nm

    def det(self):
        if len(self.m) != len(self.m[0]):
            return False
        if len(self.m) == 2:
            return self.m[0][0] * self.m[1][1] - self.m[1][0] * self.m[0][1]

        d = 0
        for i in range(len(self.m[0])):
            nm = self.subDet(0, i)
            factor = self.m[0][i] * nm.det()
            if i % 2 != 0:
                factor *= -1
            d += factor
        return d

    def __len__(self):
        return len(self.m) * len(self.m[0])

    def __str__(self):
        r = ""
        for i in self.m:
            r += str(i) + "\n"
        return r


matrix1 = [[-1, 1, 1, 1, 0, -2, 0],
           [-1, -3, -2, 2, -3, 1, 2],
           [0, 2, -3, 1, 2, -2, -2],
           [-1, -3, 2, 2, -3, 0, 2],
           [1, 0, -3, -3, 2, -1, 0],
           [-1, -2, -2, -1, 0, -1, -1],
           [-3, -1, -2, -2, -2, -2, 0]]
matrix2 = [
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1]

]

m = matrix(matrix1)
n = matrix(matrix2)

print(m)
print(m.det())
print(n)
print(m.transposed())

print(m * n)
print(m ** 2)
