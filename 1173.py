x = int(input())

aux = 0

if x<50:
    for i in range(1,11):
        print("N[%d] = %d"%(aux,x))
        aux += 1
        x *= 2
