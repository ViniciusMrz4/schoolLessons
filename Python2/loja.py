pag = 0
print("="*20, "Lojinha do Vini", "="*20)

preco = float(input("Valor do Produto: "))

print('''Escolha a forma de pagamento
[ 1 ] à vista com dinheiro ou cheque
[ 2 ] à vista no cartão 
[ 3 ] 2 vezes no cartão
[ 4 ] 3 vezes ou mais no cartão''')

while pag < 1 or pag > 4:
    pag = int(input("Opção de pagamento: "))
    if pag == 1:
        preco *= 0.90
        print(f"O valor total do produto com 10% de desconto é R${preco}")
    elif pag == 2:
        preco *= 0.95
        print(f"O valor total do produto com 5% de desconto é R${preco}")
    elif pag == 3:
        print(f"O valor total do produto é R${preco}")
    elif pag == 4:
        preco *= 1.20
        print(f"O valor total do produto com 20% de juros é R${preco}")
    else:
        print("Opção inválida, digite novamente por favor!")
        
print("FIM")


