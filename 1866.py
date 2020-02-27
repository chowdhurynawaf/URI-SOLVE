x = int(input())


l = [int(input()) for y in range(x)]

for numbers in l:
    if numbers%2 != 0:
        print("1")
    elif numbers%2 == 0:
        print("0")
