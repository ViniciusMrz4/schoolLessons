from datetime import date
today = date.today().year
menor = 0
maior = 0
for i in range(1, 8):
    ano = int(input("Digite o ano em que a {}ª nasceu: ".format(i)))
    idade = today - ano
    if idade >= 18:
        maior += 1
    else: 
        menor += 1
print("A quantidade de pessoa que ja atingiram a maior idade é de {}".format(maior))
print("A quantidade de pessoa que ainda não atingiram a maior idade é de {}".format(menor))
