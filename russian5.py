import random
for i in range(5):
  a = random.randrange(30)
  b = random.randrange(100)
  c = "ロ・"
  d = "ロシアン・ルーレット"
  if b <= 10:
    c = "ギャ・"
    d = "ギャン泣き・ルーレット"
  print(c*a+d)
