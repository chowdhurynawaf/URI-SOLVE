l = []

X = int(input())

for i in range(X):
    l.append(int(input()))

for n in l:
    if(n%2!=0 and n<0):
         print("ODD NEGATIVE")
    if(n%2 != 0 and n>0):
         print("ODD POSITIVE")

    if n==0:
         print("NULL")

    if(n%2 == 0 and n>0):
         print("EVEN POSITIVE")
    if(n%2 == 0 and n<0):
         print("EVEN NEGATIVE")

