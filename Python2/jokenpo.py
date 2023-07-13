from random import randint
from time import sleep

jogador = 4

while (jogador > 3 or jogador < 1):       
    pc = randint(1, 3)
    print('''Suas opções:
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA''')

    jogador = int(input("Escolha a sua jogada: "))

    if jogador > 3 or jogador < 1:
        print("Digite um valor valido!")
        continue

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!!")
    sleep(1)

    if jogador == pc:
        print("Empate!")
    elif jogador == 1 and pc == 2:
        print("Você escolheu PEDRA e o computador PAPEL")
        print("O computador venceu!")
    elif jogador == 1 and pc == 3:
        print("Você escolheu PEDRA e o computador TESOURA")
        print("Voce venceu!")
    elif jogador == 2 and pc == 1: 
        print("Você escolheu PAPEL e o computador PEDRA")
        print("Voce venceu!")
    elif jogador == 2 and pc == 3:
        print("Você escolheu PAPEL e o computador TESOURA")
        print("O computador venceu!")
    elif jogador == 3 and pc == 1:
        print("Você escolheu TESOURA e o computador PEDRA")
        print("O computador venceu!")
    elif jogador == 3 and pc == 2:
        print("Você escolheu TESOURA e o computador PAPEL")
        print("Voce venceu!")

print("FIM")