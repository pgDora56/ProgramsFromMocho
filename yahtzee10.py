import random
for k in range(10):
 a = ''
 for i in range(5):
  a += str(random.randrange(1,7,1))
 if int(a)%11111==0:
  a +=' ヤッツィー'
 b=sorted(list(map(int,a)))
 if b == [1,2,3,4,5] or b == [2,3,4,5,6]:
  a +=' 大きいストレート'
 print(a)
