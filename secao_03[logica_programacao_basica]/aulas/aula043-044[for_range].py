print(100 * "=")

inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite o passo: "))

print(100 * "=")

for numero in range(inicio, fim, passo):
    print(numero, end=" -> ")

print("ACABOU!!")
print(100 * "=")
