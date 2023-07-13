from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento do atleta: "))
idade = atual - nasc
print(f"O atleta tem {idade} anos de idade")
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JÚNIOR")
elif idade <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")