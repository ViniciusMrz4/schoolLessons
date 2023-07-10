km = int(input("Digite a distancia de dessa viagem: "))
if km <= 200: 
    preco = (km * 0.50)
else: 
    preco = (km * 0.45)
print(f"Você fará uma viagem de {km}KM")
print("O preço da passagem será de {:.2f} reais".format(preco))