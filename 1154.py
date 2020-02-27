X = 0
Y = 0
Z = 0

while True:
    Z = int(input())

    if Z>0:
        X = X+Z
        Y = Y+1
    else:
        break
print("%.2f"%(X/Y))

