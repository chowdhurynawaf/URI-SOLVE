
x = int(input())
l = [int(x) for x in input().split()]

m,p = l[0],0

for i in range(x):
    if l[i]<m:
            m,p = l[i],i
print(p+1)
