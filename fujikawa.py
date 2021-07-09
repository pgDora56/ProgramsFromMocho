from random import randrange 
def okawaxji(a,b,n):
  if n == 0:
    return a + b
  else:
    return okawaxji(a+"川", b+"児", n-1)

print(okawaxji("藤","球",randrange(1,11)))
