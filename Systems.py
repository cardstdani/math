import numpy as np

s = """3x+2y+z=1
5x+3y+4z=2
x+y-z=1"""

a = []
a2 = []
d = {}
c = []

var = ""
for y in s:
  if y.isalpha():
    var += y
  else:
    if var != "":
      d[var] = []
      var = ""

for i in s.split("\n"):
  spl = i.split("=")
  c.append(float(spl[1]))
  
  w = spl[0]
  temp = ""
  vars = list(d.keys())
  for x in range(len(w)):
    if w[x].isalpha():
      if w[x] in vars:
        d[w[x]].append(float(temp) if temp != "" and temp != "+" and temp != "-" else (1.0 if temp == "+" or temp == "" else -1.0))
        vars.remove(w[x])
      else:
        d[w[x]][len(d[w[x]])-1] += (float(temp) if temp != "" and temp != "+" and temp != "-" else (1.0 if temp == "+" or temp == "" else -1.0))        
      temp = ""
    else:
      temp += w[x]
  for y in vars:
    d[y].append(0.0)

for i in d.values():
  a.append(i)
  a2.append(i)

a2.append(c)
a = np.matrix(a, dtype=np.float).T
a2 = np.matrix(a2, dtype=np.float).T
c = np.matrix(c).reshape(-1, 1)

print(d)
print(a)
print(a2)

rankA = np.linalg.matrix_rank(a)
rankA2 = np.linalg.matrix_rank(a2)
unknown = len(d.keys())

if rankA == rankA2 == unknown:
  detA = np.linalg.det(a)
  for i in range(len(d.keys())):
    solution = np.matrix(a)    
    solution[:, i] = c
    print(list(d.keys())[i], "=", np.linalg.det(solution) / detA)
