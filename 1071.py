l = []

a = int(input())

b = int(input())

for i in range(b+1,a):
    if i%2 != 0:
        l.append(i)

b = sum(l)

print(b)
