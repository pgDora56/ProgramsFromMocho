import random
lis = ['は？','キレた','ID','控えた']
while True:
 seq=random.sample(lis,4)
 count=0
 for i in range(4):
  print(seq[i])
  if seq[i] != lis[i]:
   break
  count += 1
 if count==4:
  print('sing0421')
  exit()
