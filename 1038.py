a,b = input().split(" ")

a = int(a)
b = int(b)

if a == 1:
    print("Total: R$ %.2f"%(4.00*b))
elif a == 2:
    print("Total: R$ %.2f"%(4.50*b))
elif a == 3:
    print("Total: R$ %.2f"%(5.00*b))
elif a == 4:
    print("Total: R$ %.2f"%(2.00*b))
elif a == 5:
    print("Total: R$ %.2f"%(1.5*b))


