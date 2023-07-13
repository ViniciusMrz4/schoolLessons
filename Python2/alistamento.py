from datetime import date
atual = date.today().year
ano = int(input("Ano de nascimento: "))
idade = atual - ano
print(f"Sua idade é de {idade} anos")
if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para você se alistar")
elif idade == 18: 
    print("Você se alistou ou deveria se alistar esse ano")
else: 
    print(f"Você deveria ter se alistado há {idade - 18} anos")