import random
for i in range (10):
 a =random.random()
 print("大分大学" if a<=0.48 else ("大阪大学" if a >=0.52 else "大同大学"))
