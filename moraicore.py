import random

def morai():
  adan = ["あ","い","う","え","お"]
  res = ""
  for _ in range(5):
    res += random.choice(adan)

  if res == "ええいああ":
    res += " 君から「もらい泣き」"

  return res
