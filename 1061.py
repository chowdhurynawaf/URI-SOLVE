d = input()
diax = d.split()
inicio = input().split(" : ")
d2 = input()
diay = d2.split()
final = input().split(" : ")

dia1 = int(diax[1])
dia2 = int(diay[1])

horaI = int(inicio[0])
horaF = int(final[0])
minuI = int(inicio[1])
minuF = int(final[1])
seguI = int(inicio[2])
seguF = int(final[2])

if dia1<=dia2:
  W = (dia2 - dia1)
if (horaI<horaF) or (horaI - horaF) == 0:
  X = (horaF - horaI)
if minuI <= minuF:
    Y = (minuF - minuI)
if seguI <= seguF:
    Z = (seguF - seguI)
if horaI > horaF:
    X = (24-(horaI - horaF))
    W = (W -1)
if minuI > minuF:
    Y = (60-(minuI-minuF))
    X = (X - 1)
if seguI > seguF:
    Z = (60 -( seguI - seguF))
    Y = (Y - 1)
print(W,"dia(s)")
print(X,"hora(s)")
print(Y,"minuto(s)")
print(Z,"segundo(s)")


