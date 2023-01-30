import random
from math import log, sqrt, exp

def randmax(A):
    vmax = max(A)
    index = [i for i in range(len(A)) if A[i] == vmax]
    return random.choice(index)


