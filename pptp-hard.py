import random
words = ["ポ", "プ", "テ", "ピ", "ッ", "ク"]
op = ""
while True:
  op += random.choice(words)
  if len(op) >= 7:
    if op[-7:] == "ポプテピピック":
      break
  if len(op) >= 1990:
    op += "You Lose!"
    break
print(op)
