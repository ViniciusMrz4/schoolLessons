notas = [10, 7, 3, 5, 10, 6, 8, 4, 9]

i = 0
soma = 0
while i < len(notas):
    soma += notas[i]
    i += 1
media = soma / len(notas)
print(media)