import random
m = ""
while True:
  song = "http://anison.info/data/song/"+str(random.randrange(100000))+".html"
  if len(m) + len(song) > 2000:
    break
  m += song + "\n"
print(m)
