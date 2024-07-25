import moraicore

res50 = ""
for _ in range(50):
  res50 += moraicore.morai() + "\n"
print(res50)
