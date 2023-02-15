import random
import numpy as np
from math import log, sqrt, exp

def randmax(A):
    vmax = max(A)
    index = [i for i in range(len(A)) if A[i] == vmax]
    return random.choice(index)

def movingAverage(x, n = 3):
    return np.convolve(x, np.ones(n))/n

def smooth(scores, m = 4):
    n = len(scores)
    x, y = [], []
    for i in range(m//2, n-m//2):
        l = [scores[i-m//2+k] for k in range(m)]
        x.append(i)
        y.append(np.mean(l))
    return x, y

def softmax(x, tau):
    x = np.array(x)
    e = np.exp(x / tau)
    return list(e / e.sum())