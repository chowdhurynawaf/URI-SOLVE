for i in range(3):
    s = 0
    while True:

        p = input("")
        if p == "caw caw":
            print(s)
            break
        s = s+int("".join("1" if x == "*" else "0" for x in p),2)

