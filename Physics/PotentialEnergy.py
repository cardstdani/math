class obj():
  def __init__(self, id, m, x, y):
    self.id = id
    self.m = m
    self.x = x
    self.y = y

def w(m1, m2, r):
  return (-6.67*10**-11 * ((m1*m2) / r))

def ep(g):
  e = 0

  for i in g.keys():
    for a in g[i]:
      if i in g[a]:   
        g[a].remove(i)                           
        d = ((i.x - a.x)**2 + (i.y - a.y)**2)**0.5
        epw = w(i.m, a.m, d)
        print("m {} {} = {}".format(i.id, a.id, epw))
        e += epw        
  return e

#m, x, y
data = [obj(0, 1, 0, 0), obj(1, 2, 0, 0.2), obj(2, 3, 0.2, 0.2), obj(3, 2, 0.2, 0)]
graph = {}

for i in data:
  for a in data:
    if not a == i:
      if i in graph:
        graph[i].append(a)
      else:
        graph[i] = [a]
        
print(ep(graph))
