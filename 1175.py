l = []
j = 0

for i in range(20):
    l.append(int(input()))
l.reverse()

for n in l:
    print("N[%d] = %d"%(j,n))
    j += 1


