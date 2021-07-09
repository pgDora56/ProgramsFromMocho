import random
words = ["ポ", "プ", "テ", "ピ", "ッ", "ク"]
op = ""
while True:
  op += random.choice(words)
  if len(op) >= 7:
    if op[-7:] == "ポプテピピック":
      break
print(f"{op[-1990:]}{len(op)}")
