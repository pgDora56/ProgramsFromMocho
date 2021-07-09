import random
kub = ["神", "戸", "高","校"]
op = ""
while True:
  op += random.choice(kub)
  if len(op) >= 4:
    break
print(op)
