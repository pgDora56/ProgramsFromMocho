import random
i = random.randrange(1,105)
res = 1
if i % 5 == 0:
 res = 2
if i % 10 == 0:
 res += 1
if i % 11 == 0:
 res = 5
if i % 55 == 0:
 res = 7
print(str(i)+"\n"+"牛"+str(res)+"頭!!")
