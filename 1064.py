l = []
p=[]

sumation = 0



for i in range(6):
    l.append(float(input()))
for n in l:
    if n>1:
        sumation = sumation+1
        p.append(n)


print("%d valores positivos"%sumation)

b = sum(p)



print("%0.1f"%(b/sumation))



