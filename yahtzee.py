import random
a = ''
for i in range(5):
 a += str(random.randrange(1,7,1))
print(a)
if int(a)%11111==0:
 print('ヤッツィー')
 exit()
b=sorted(list(map(int,a)))
if b == [1,2,3,4,5] or b == [2,3,4,5,6]:
 print('大きいストレート')
