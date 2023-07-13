casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do salário: "))
anos = int(input("Digite quantos anos de financiamento: "))
prestacao = casa / (anos * 12)

print("Para pagar uma casa de {:.2f} reais em {} anos".format(casa, anos))
print("O valor da prestação será de {:.2f} reais".format(prestacao))

salario = salario * 0.30

print("30% do seu salário equivale a {:.2f} reais".format(salario))

if salario < prestacao:
    print("O seu emprestimo foi negado!")
else: 
    print("O seu emprestimo foi aprovado!")