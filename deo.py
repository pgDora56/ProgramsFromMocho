import random
ktkn = [chr(i) for i in range(ord("ァ"), ord("ヴ")+1)]
cho = "".join(random.sample(ktkn, 2))
cho2 = ""
for i in range(10):
  cho2 += cho
print(cho2)
