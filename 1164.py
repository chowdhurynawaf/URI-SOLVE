x = int(input())

for i in range(x):
    inp = int(input())
    sum = 0
    for k in range(1,inp):
        if inp%k == 0:
            sum += k

    if sum == inp:
        print("%d eh perfeito"%inp)
    else:
        print("%d nao eh perfeito"%inp)
