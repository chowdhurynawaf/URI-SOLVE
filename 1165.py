x = int(input())

for i in range(x):
    a = int(input())
    primo = True

    for j in range(2,a):
        if(a%j)==0:
            primo = False

    if(primo):
        print("%d eh primo"%a)
    else:
        print("%d nao eh primo"%a)
