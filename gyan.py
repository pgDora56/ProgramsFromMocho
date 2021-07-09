import random

def gyan_roulette():
  who = ["sing"] * 10 + ["かりゅうど"]
  where = ["梅田", "京都", "キョン亭", "Discord", "夢幻", "中野", "幕張"]
  print(random.choice(who) + "が" + random.choice(where) + "でｷﾞｬﾝ泣き")

if __name__ == "__main__":
  gyan_roulette()
