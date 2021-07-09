import random
thd = ["東", "阪", "大"]
op = ""
while True:
  op += random.choice(thd)
  if len(op) >= 4:
    break
print(op)
