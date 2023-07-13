peso = float(input("Peso em Kg: "))
altura = float(input("Altura em M: "))

imc = peso / (altura ** 2)

print(f"Seu peso é de {peso}kg, sua altura é de {altura}m e seu IMC é igual a {imc}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40: 
    print("Obesidade")
else: 
    print("Obesidade mórbida")