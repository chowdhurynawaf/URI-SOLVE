cont = 0

while (cont<1):
  
  x, y = map(int, input().split())
  
  listNum = []
  
  if x>0 and y>0:
    if (x<y):
      for n in range(x, y+1):
        listNum.append(n)
        res = " ".join(map(str, listNum))
        soma = sum(listNum)
      print(res, "Sum=%d" %soma)
      listNum = []
    
    elif (x>y):
      for n in range(y, x+1):
        listNum.append(n)  
        res = " ".join(map(str, listNum))
        soma = sum(listNum)
      print(res, "Sum=%d" %soma)
      listNum = []
  
  else:
    cont+=1
  
  
  
