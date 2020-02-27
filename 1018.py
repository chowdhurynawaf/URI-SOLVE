n = int(input())
print(n)
if n >= 0 and n < 1000000:
  ncem = n//100
  n = n%100
  print("%i nota(s) de R$ 100,00"%ncem)
if n >= 0 and n < 1000000:
  ncinq = n//50
  n = n%50
  print("%i nota(s) de R$ 50,00"%ncinq)
if n >= 0 and n < 1000000:
  nvin = n//20
  n = n%20
  print("%i nota(s) de R$ 20,00"%nvin)
if n >= 0 and n < 1000000:
  ndez = n//10
  n = n%10
  print("%i nota(s) de R$ 10,00"%ndez)
if n >= 0 and n < 1000000:
  ncinc = n//5
  n = n%5
  print("%i nota(s) de R$ 5,00"%ncinc)
if n >= 0 and n < 1000000:
  ndoi = n//2
  n = n%2
  print("%i nota(s) de R$ 2,00"%ndoi)
if n >= 0 and n < 1000000:
  num = n//1
  n = n%1
  print("%i nota(s) de R$ 1,00"%num)

