import random
sx = ""
while True:
  sx += random.choice(["ダ", "ﾀﾞ"])
  if random.random() < 0.01: break
sx += "ダーン!"
print(sx)
