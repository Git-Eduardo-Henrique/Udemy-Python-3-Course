print(100 * "=")

nome = input("Digite seu nome: ")
encontrar = input("Oque você quer encontrar? ")

print(100 * "=")

# in = verificar se algo está em algo
# not in = faz o oposto
if encontrar in nome:
    print(f"{encontrar} está em {nome} ;)")
else:
    print(f"{encontrar} não está em {nome} :<")

print(100 * "=")