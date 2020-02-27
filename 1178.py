x = float(input())
print("N[0] = %.4f"%x)

for i in range(1,100):
    x=x/2
    print("N[%d] = %.4f"%(i,x))
