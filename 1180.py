
qte = int(input())
lista = list(map(int,input().split()))

less = min(lista)
index = lista.index(min(lista))

print("Menor valor: %d"%less)
print("Posicao: %d"%index)
