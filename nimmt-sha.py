import random
res =0
for j in range(6):
 i = random.randrange(1,105)
 res += 1
 if i % 5 == 0:
  res += 1
 if i % 10 == 0:
  res += 1
 if i % 11 == 0:
  res += 4
 if i % 55 == 0:
  res += 1
 print(i)
 if j==0 and i==104:
  print("初手104")
print("牛"+str(res)+"頭!!")
if res >= 15:
 print("ありあまる牛")
