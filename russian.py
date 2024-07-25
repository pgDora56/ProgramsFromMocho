import random
a = random.randrange(30)
b = random.randrange(100)
c = "ロ・"
d = "ロシアン・ルーレット"
if b <= 10:
  c = "ギャ・"
  d = "ギャン泣き・ルーレット"
if c*a+d == "ギャ・ギャ・ギャ・ギャン泣き・ルーレット":
  print("梅田で")
print(c*a+d)
