# Created by Dora at 2022-06-08 21:45:00
import random

scramble = ["U", "L", "R", "F", "B", "D"]
count = ["", "2", "'"]

prev = ""
c = ""
res = ""
for i in range(20):
    while prev == c:
        c = random.choice(scramble)
    prev = c
    res += f"{c}{random.choice(count)} "
print(res)
