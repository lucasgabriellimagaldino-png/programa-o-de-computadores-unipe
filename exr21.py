n = (int(input("Digite uma nota: ")))
while n < 0 or n > 10:
    print("Valor inválido, digite novamente")
    n = (int(input("Digite uma nota: ")))
print("Valor válido")    
