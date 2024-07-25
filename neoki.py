import random
dic = {
  "ﾈ" : ["ﾈ", "ｵｷ", "ﾃ"],
  "ｵｷ" : ["ﾈ", "ｵｷ", "ﾃ"],
  "ﾃ" : ["ﾈ", "ｵｷ"]
}
prev = "ﾈ"
op = "ﾈ"
while True:
  prev = random.choice(dic[prev])
  op += prev
  if len(op) > 20:
    if random.random() > 0.8:
      break
print(op)
