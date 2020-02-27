while True:
    n = [int(x) for x in input("").split()]
    if n[0] == 0: break
    d, i = n[0] * n[1], 0
    e = (d * 100) / n[2]
    f = pow(e,0.5)
    print("%d"%f)
