sal = float(input("Digie o valor do salario do funcionário: "))
if sal <= 1250:
    sal = sal * 1.15
else:
    sal = sal * 1.10
print(f"O salário do funcionario é de {sal:.2f}")