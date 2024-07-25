import random
point = 65
for k in range(5):
 res =0
 nu = []
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
  nu.append(str(i))
  if j==0 and i==104:
   print("初手104")
 s =" ".join(nu)
 print(s)
 cow = "牛"+str(res)+"頭!!"
 point -= res
 if res >= 15:
  cow += " ありあまる牛"
 print(cow)
print(point)
if point <= 0:
 print("sinちゃん「はい負け〜〜〜」")
