import random
pretender = ["グッバイ", "君の", "運命の", "ひとーは", "ぼーく", "じゃない～", "つらーいけど", "いなめない", "でもはなれがたい", "のさ"]

ly = "茜屋「"
lim = 2
if random.randrange(len(pretender)) < lim:
    ly += "ｹﾞｪｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰ"
else:
    for i in pretender:
        ly += i
        if random.randrange(len(pretender)) < lim:
            ly += "ｹﾞｪｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰ"
            break
        ly += " "
ly += "」"
print(ly)
