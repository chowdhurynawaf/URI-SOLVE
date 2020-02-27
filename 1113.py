x, y = map(int, input().split(" "))

while (x!=0 and y!=0):
  if (x>y):
    print("Decrescente")
    x, y = map(int, input().split(" "))
  elif (x<y):
    print("Crescente")
    x, y = map(int, input().split(" "))
  else:
    break

