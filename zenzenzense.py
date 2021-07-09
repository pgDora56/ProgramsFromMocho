import random
a = 3
for i in range(30):
  r = random.randrange(2)
  if r == 1:
    a += 1
  elif a <= 0:
    pass
  else:
    a -= 1
print("前"*a+"世")
