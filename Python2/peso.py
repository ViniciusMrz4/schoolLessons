menor = 0
maior = 0
for i in range(0, 5):
    peso = float(input(f"Peso da {i}ª pessoa em kg: "))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso foi de {maior}kg e o menor foi de {menor}kg")
