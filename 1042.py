a , b , c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

big = max(a,b,c)
less = min(a,b,c)

mid = (a+b+c )-(big+less)

print("%d\n%d\n%d\n\n%d\n%d\n%d"%(less,mid,big,a,b,c))
