import numpy as np

o = int(np.random.normal(5,3))
x = int(np.random.normal(5,3))

if o < 1: o = 1
if x < 1: x = 1
print(o, "o", x, "x")
