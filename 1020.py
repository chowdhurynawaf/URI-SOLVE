#URI Online Judge | 1020 Idade em Dias
x = int(input())
#Anos
Anos = x // 365
resto = x % 365
#Meses
Meses = resto // 30
resto %= 30
#Dias
Dias = resto // 1
print('%d ano(s)\n%d mes(es)\n%d dia(s)' %(Anos, Meses, Dias))
