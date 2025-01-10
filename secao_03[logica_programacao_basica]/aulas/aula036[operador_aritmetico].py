contador = 0

print(100 * "=")
print("contador de 1 até 10")
print(100 * "=")

while contador < 10:
    # += soma o valor com o que estava na variavel (variavel = variavel + 1)
    # outros: -= *= **= /= //= %=
    contador += 1
    print(contador, end=" -> ")

print("ACABOU!")
print(100 * "=")