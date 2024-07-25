import random

def koube():
  kub = ["こう", "べ"]
  op = ""
  while True:
    op += random.choice(kub)
    if len(op) >= 7:
      break
  print(op)
  if op == "こうべこうこう":
    print("天王寺高校")
  elif op == "べべべべべべべ":
    print("通行止のお知らせ　29日午後4時18分より国道40号ばばばばばばえおうぃおい～べべべべべべべべべえべえええべえべべべえ（9.9km）で通行止を実施しています")

if "__name__" == "__main__":
  koube()
