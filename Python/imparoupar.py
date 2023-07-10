n = int(input("Digite um numero inteiro: "))
i = n % 2 == 0
if i == True: 
    print("O numero {} é par!".format(n))
else:
    print("O numero {} é impar!".format(n))