print(100 * "=")

nome = input("digite seu nome: ")
dindin = int(input("quanto dinheiro voce tem: "))

print(100 * "=")

# > = adiciona caracteres na esquerda
# x = converte para hexadecimal

print(f"{nome} tem R$ {dindin:0>4}")
print(f"Hexadecimal de {dindin}: {dindin:08x}")

print(100 * "=")