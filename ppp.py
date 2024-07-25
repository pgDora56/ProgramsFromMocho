# Created by ぱち at 2022-01-28 05:55:16
import random
words = ["ぽ", "っ", "ぴ", "ー"]
op = ""
while True:
  op += random.choice(words)
  if len(op) >= 6:
    if op[-6:] == "ぽっぴっぽー":
      break
print(f"{op[-1990:]}{len(op)}")
