sum = 1
up = 3
down = 2

while up<40:
    sum = sum+float(up)/float(down)
    down *= 2
    up = up+2
print("%.2f"%sum)
