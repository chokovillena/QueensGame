import numpy as np
def printArray(args):
    print "\t".join(args)

n = 10

Array = np.zeros(shape=(n,n)).astype('int')

for row in Array:
    printArray([str(x) for x in row])
