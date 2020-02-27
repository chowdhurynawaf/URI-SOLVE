X = int(input())

if 1 <= X <= 1000:
    for i in range(1,X):
        if i%2 != 0:
            print(i)
if X%2 != 0:
    print(X)

