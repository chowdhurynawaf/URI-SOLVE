a = input()

b = list(a)

c =0



for i in b:
    if i == "1":
        c += 1

if c%2==0:
    print(str(a)+str(0))
elif c%2 != 0:
    print(str(a)+str(1))

