a = int(input())
sum = 0


for i in range(a):
    b,c = map(int,input().split())
    if b == 1001:
        b = 1.50
    elif b == 1002:
        b = 2.50
    elif b == 1003:
        b = 3.50
    elif b == 1004:
        b = 4.50
    elif b == 1005:
        b = 5.50

    sum += b*c

print("%.2f"%sum)
