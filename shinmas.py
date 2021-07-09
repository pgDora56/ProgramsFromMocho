import random
lis = ["新間"] * 500
lis.append(random.choice(["新聞", "薪間", "析間"]))
random.shuffle(lis)
print("".join(lis))
