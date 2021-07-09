import glob

l = glob.glob('programs/*.py')
asc = []
for f in l:
  asc.append(f[9:-3])
asc.sort()
print("\n".join(asc))
