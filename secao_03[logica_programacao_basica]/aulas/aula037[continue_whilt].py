contador = 0

print(100 * "=")
print("contador de 1 até 10")
print(100 * "=")

while contador < 10:
    contador += 1

    # continue = para o while em uma parte espesifica
    if contador == 6:
        continue

    print(contador, end=" -> ")

print("ACABOU!")
print("vixi, esqueci do 6...")
print(100 * "=")