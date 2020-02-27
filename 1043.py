valores = input().split(" ")

a, b, c = valores


if ((float(b) - float(c)) < float(a) < (float(b) + float(c)) and (float(a) - float(c)) < float(b) < (float(a) + float(c)) and (float(a) - float(b)) < float(c) < (float(a) + float(b))):
  
  soma_perm = float(a) + float(b) + float(c)
  print("Perimetro = %0.1f" %soma_perm)

else:
  
  soma_trap = (float(a) + float(b)) * float(c) / 2
  print("Area = %0.1f" %soma_trap)

