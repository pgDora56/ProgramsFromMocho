import random
chars = list("顰蹙")
st = ""
for _ in range(20):
  st += random.choice(chars)
print(st)
