velho = 0
media = 0
quantas = 0
for i in range(1, 5):
    print(f"-----{i}° PESSOA -----")
    nome = input("Nome: ").strip
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip
    if sexo == "M" and idade > velho:
            velho = idade
            nomevelho = nome
    if sexo == "F" and idade < 20:
        quantas += 1
    media += idade
media = media/i
print("A média de idade do grupo é de {:.2} anos".format(media))
print(f"O homem mais velho se chama {nomevelho} e tem {velho} anos de idade")
print(f"Ao todo temos {quantas} mulhere(s) que tem menos de 20 anos de idade")
