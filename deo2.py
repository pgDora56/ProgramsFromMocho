import random
ktkn = [chr(i) for i in range(ord("ァ"), ord("ヴ")+1)]
cho = "".join(random.sample(ktkn, 2))
cho2 = ""
l =random.randrange(30)
for i in range(l):
    cho2 += cho
print(cho2)
