nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2
print(f"Sua média é igual {media}")
if media < 5:
    print("Reprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
else:
    print("Aprovado")