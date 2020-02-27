X = int(input())
l = []
sum = 0
out = 0

for i in range(X):
    l.append(input())

li = map(int ,l)

for n in li:
    if (10<= n <= 20):
        sum += 1
    else:
        out += 1

print(sum,"in")
print(out,"out")


