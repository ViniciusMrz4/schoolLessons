cidade = input("Insira o nome da cidade: ").strip()
f = cidade[:5].upper() == "SANTO"
if f == True:
    print("Essa cidade começa com Santo")
else:
    print("Essa cidade não começa com Santo")