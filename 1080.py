l = []
for i in range(1,101):
    l.append(int(input()))

map(int,l)


highest = max(l)

position = l.index(highest)

print(highest)
print(position+1)
