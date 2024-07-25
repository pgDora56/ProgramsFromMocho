import random

def roulette(letters):
  unit = ""
  while len(unit) <= 2000:
    unit += random.choice(letters)
    if len(unit) >= len(letters):
      if unit[(-1*len(letters)):]==letters:
        break
  print(unit[:2000])
