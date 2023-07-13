opcao = 4
num = int(input("Digite um numero inteiro: "))
print('''Escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')

while (0 < opcao > 3):
    opcao = int(input("Sua opção: "))
    if opcao == 1:
        print("{} convertido para binário é igual a {}".format(num, bin(num)[2:]))
    elif opcao == 2:
        print("{} convertido para octal é igual a {}".format(num, oct(num)[2:]))
    elif opcao == 3:
        print("{} convertido para hexadecimal é igual a {}".format(num, hex(num)[2:]))
    else: 
        print("Opção inválida, por favor tente novamente")
print("FIM!")