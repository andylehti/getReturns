def getReturns(*f): return [i for f, args in f for i in f(*args)]

def exampleA(a, b): return a, b, a + b, a, b
def exampleB(a, b): return a * 2, b * 2

r = getReturns((exampleA, (1, 2)), (exampleB, (3, 4))) # function name (with args), separated by commas
print(r)
