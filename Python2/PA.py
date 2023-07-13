num = int(input("Primeiro Termo: "))
raz = int(input("Razão: "))
decimo = num + (10 - 1) * raz
for i in range (num, decimo + raz, raz):
    print(f"{i} -> ", end="")
print("ACABOU")