import random
ktkn = [chr(i) for i in range(ord("ァ"), ord("ヴ")+1)]
l =random.randrange(30)
for j in range(10):
 cho = "".join(random.sample(ktkn, 2))
 cho2 = ""
 for i in range(l):
    cho2 += cho
print(cho2)
