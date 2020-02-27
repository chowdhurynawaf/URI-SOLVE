lista = list(map(int, input().split()))
j = 0
l = []

for n in lista:
    if n>0:
        l.append(n)
x = int(l[0])
y = int(l[1])



for i in range(y):
    j = j+i+x

print(j)
