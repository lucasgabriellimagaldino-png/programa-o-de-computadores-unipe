n1 = int(input("Digite um número: "))
if  n1 % 2 == 0 and n1 > 0:
    print("Par positivo")
elif n1 % 2 == 0 and n1 < 0:
    print("Par negativo")
elif n1 % 2 != 0 and n1 > 0:
    print("Ímpar positivo")    
elif n1 % 2 != 0 and n1 < 0:
    print("Ímpar negativo")
else:
    print("O número é neutro")   