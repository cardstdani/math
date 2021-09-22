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
      #Sum
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
    #Scalar by matrix multiplication   
    for i in range(len(self.m)):
        for j in range(len(self.m[i])):
          self.change(i, j, self.m[i][j] * n)
    return self
  
  def __mul__(self, n):    
    #Matrix multiplication
    if (len(self.m[0]) == len(n.m)):
      o = []
      for i in range(len(self.m)):
        o.append([])
        for j in range(len(n.m[0])):
          o[i].append(self.getRowByColumn(i, j, n))
      self.setMatrix(o)
      return self
  
  def getRowByColumn(self, row, column, n):
    r = 0
    for i in range(len(self.m[row])):
      r += self.m[row][i] * n.m[i][column]
    return r

  def __len__(self):
    return len(self.m) * len(self.m[0])
  
  def __str__(self):    
    r = ""
    for i in self.m:      
      r += str(i) + "\n"
    return r

matrix1 = [
             [0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]
]
matrix2 = [
             [-1, 0, 0],
             [0, -1, 0],
             [0, 0, -1]

]

m = matrix(matrix1)
n = matrix(matrix2)

print(m)
print(n)
print(m.transposed())

print(m*n)
