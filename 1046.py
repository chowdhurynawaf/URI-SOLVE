val = input().split(" ")
a, b = val

a = int(a)
b = int(b)

if (a >= b):
  calc1 = (24 - a) + b
  print("O JOGO DUROU %d HORA(S)" %calc1)

else:
  calc2 = b - a
  print("O JOGO DUROU %d HORA(S)" %calc2)

