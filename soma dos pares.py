soma = 0
cont = 0
for c  in range (0, 6):
    num = int(input("Digite um numero: "))
    if num  % 2 == 0:
        soma += num
        cont += 1
print(f"A soma dos {cont} numeros pares que foram digitados é {soma}")
