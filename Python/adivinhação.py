import random
n = random.randint(0, 5)
print("O computador pensou em um número de 0 a 5")
chute = int(input("Tente adivinhar o numero que o computador pensou: "))

if chute == n:
    print("Você venceu o computador")
else:
    print("Você perdeu, o cumputador pensou no numero {}".format(n))

