from random import randint
num = randint(1, 10)
tentativas = 0
acertou = False
print("Acabei de pensar em um número de 1 a 10\nSerá que você consegue adivinhar qual é?")
while not acertou:
    palp = int(input("Qual é o seu palpite? "))
    tentativas += 1
    if palp == num: 
        acertou = True
    elif palp > num:
        print("Menos. Tente novamente.")
    else:
        print("Mais. Tente novamente.")
print("\nMuito bem, você acertou com {} tentativa(s)!".format(tentativas))
