sum = 0
qte = 0

while qte<2:
    nota = float(input())
    if (nota>=0  and nota<=10):
        sum += nota
        qte += 1
    else:
        print("nota invalida")
print("media = %.2f"%(sum/qte))


