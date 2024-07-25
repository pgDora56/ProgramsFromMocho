import random
msg = ""
while len(msg) < 2000:
  msg += "もちょだよ！\n"
  if random.random() < 0.1: break
print(msg)
