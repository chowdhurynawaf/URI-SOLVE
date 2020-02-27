l = []

sum = 0

for i in range(5):
    l.append(int(input()))
for n in l:
    if n%2==0:
        sum = sum+1


print("%d valores pares"%sum)
