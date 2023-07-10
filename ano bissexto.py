ano = 0
from datetime import date
ano = int(input("Digite o ano que você quer analisar: "))
if ano == 0:
    ano = date.today().year   
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0: 
    print("Digite o ano que você digitou é bissexto")
else:
    print("Digite o ano que você digitou não é bissexto")
