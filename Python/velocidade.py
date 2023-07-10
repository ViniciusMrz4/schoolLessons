velocidade = float(input("Qual a velocidade atual do carro? "))
if velocidade > 80:
    print("Você foi multado! Excedeu o limete de velocidade de 80KM/H")
    velocidade -= 80
    multa = velocidade * 7
    print(f"Você foi multado em {multa:.2f} reais")
print("Tenha um bom dia e dirija com segurança")