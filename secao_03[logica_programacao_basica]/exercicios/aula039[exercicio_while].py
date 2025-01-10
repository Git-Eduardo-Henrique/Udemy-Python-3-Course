contador = 0
nova_string = "|"

print(100 * "=")

digitado = input("digite algo para ver seus caracteres: ")

print(100 * "=")

while contador < len(digitado):
    nova_string += f" {digitado[contador]} |"
    contador += 1

print(f"{digitado} com caracteres separados: {nova_string}")
print(100 * "=")