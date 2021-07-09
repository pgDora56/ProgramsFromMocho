import random
words = ["ポ", "プ", "テ", "ピピック"]
op = ""
while True:
  op += random.choice(words)
  if len(op) >= 7:
    if op[-7:] == "ポプテピピック":
      break
print(op)
