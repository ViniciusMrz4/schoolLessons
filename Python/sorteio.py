from random import choice
n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")
nomes = [n1, n2, n3, n4]

escolhido = choice(nomes)
print(f"O aluno escolhido foi {escolhido}")