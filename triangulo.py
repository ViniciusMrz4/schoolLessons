a = float(input("Primeiro seguimento: "))
b = float(input("Segundo seguimento: "))
c = float(input("Terceiro seguimento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os seguimentos acima PODEM formar um triângulo")
    if a == b == c:
        print("Os seguimentos acima formam um triangulo equilátero", end="")
    elif a != b!= c != a:
        print("Os seguimentos acima formam um triangulo isósceles", end="")
    else:
        print("Os seguimentos acima formam um triangulo escaleno", end="")
else: 
    print("Os seguimentos acima NÂO PODEM formar um triangulo")