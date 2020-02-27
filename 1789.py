aux = 1

while True:
  try:
    x = int(input())
    if x>=1 and x<=500:
      lesmas = input()
      grupo = lesmas.split()
  
    for elemento in grupo:
      if int(elemento)>=1 and int(elemento)<=50:
        if int(elemento)>aux:
          aux = int(elemento)
  
    if aux<10:
      print("1")
    if aux>=10 and aux<20:
      print("2")
    if aux>=20:
      print("3")
    
    aux = 0
    
  except:
    break
