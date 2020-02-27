l = []

for i in range(5):
    l.append(input())

new_list = map(int,l)

#a,b,c,d,e = new_list

i = 0
pares = 0
impares = 0
positivos = 0
negativos = 0

for n in new_list:
    if n%2 == 0:
        pares += 1
    if n%2 != 0 :
        impares += 1
    if n>0:
        positivos += 1
    if n<0:
        negativos += 1

print("%d valor(es) par(es)" %pares)
print("%d valor(es) impar(es)" %impares)
print("%d valor(es) positivo(s)" %positivos)
print("%d valor(es) negativo(s)" %negativos)





