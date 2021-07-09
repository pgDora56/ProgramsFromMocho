import random
lis = []
for i in range(10):
  rand_val = random.random()
  if rand_val < 0.93:
    lis.append("sinちゃん起きて！！")
  elif rand_val < 0.95:
    lis.append("sinちゃん起きてすぐ寝て！！")
  else:
    lis.append("sinちゃん寝て！！")
print("\n".join(lis))
