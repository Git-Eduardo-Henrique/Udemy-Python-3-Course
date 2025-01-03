lista_nomes = ["Eduardo", "Theo", "Tatiana", "Claudio", "Maura"]
cont = 0

print(100 * "=")
print(f"lista de nomes: {lista_nomes}")
print(100 * "=")
print(f"nomes separados e por index:")
print(100 * "=")

for nome in lista_nomes:
    print(f"index {cont} | nome: {nome}")
    cont += 1

print(100 * "=")
