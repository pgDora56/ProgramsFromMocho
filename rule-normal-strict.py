# Created by Dora at 2021-08-19 09:49:47
import numpy as np
o = -1
x = -1
while o < 3:
  o = int(np.random.normal(8,3))
half_o = o // 2
while x < 1:
  x = int(np.random.normal(half_o, half_o // 2))

print(o, "o", x, "x")
