#f(x)=A*(r**i)
def simpleExponentialGrowth(initialAmount=10, rate=1.1, iterations=2):
  return initialAmount*(rate**iterations)

def compoundedExponentialGrowth(initialAmount=300, rate=0.045, divisions=2, iterations=7):
  return initialAmount*(1+(rate/divisions))**(divisions*iterations)

def compoundedExponentialDecay(initialAmount=300, rate=0.045, divisions=2, iterations=7):
  return initialAmount*(1-(rate/divisions))**(divisions*iterations)

print(simpleExponentialGrowth(200, 1.03, 10))
print(compoundedExponentialGrowth(1200, 0.06, 12, 3))
