import random
def main(i):
  print("ぼく「寝てもいいですか？」")
  for _ in range(i):
    print(random.choice(["ﾈﾃﾓｲｲ"]+["ﾀﾞﾝﾒｪ!!"]*10000))

if __name__ == "__main__":
  main(1)
