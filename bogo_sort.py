# Created by Dora at 2022-07-22 03:54:34
import random
cont = True
cnt = 0
l = [i for i in range(5)]
while cont:
  random.shuffle(l)
  cnt += 1
  prev = l[0]
  for x in l:
    if prev > x:
      break
    prev = x
  else:
    cont = False
print("Bogo count:", cnt)
