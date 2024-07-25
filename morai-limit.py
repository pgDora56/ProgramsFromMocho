import moraicore
cnt = 0
r = ""
all = ""
while r != "ええいああ 君から「もらい泣き」":
  cnt += 1
  r = moraicore.morai()
  all += r + "\n"
if len(all) > 1000: print(all[:500] + "..." + all[-500:])
else: print(all)
print(cnt)
