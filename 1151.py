x = int(input())
s = 0
s2 = 1
temp = 0
print(s,s2,end=" ")

for i in range(x-3):
    temp = s+s2
    print(temp,end=" ")
    s = s2

    s2 = temp
if temp>0:
    print(s+s2)





