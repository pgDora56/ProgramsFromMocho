def main(command):
  print("`"+"`"+"`py")
  with open(f"programs/{command}.py") as f:
    print(f.read())
  print("`"+"`"+"`")

if __name__ == "__main__":
  print("Usage: `import nakami` and `nakami.main([command])`")
