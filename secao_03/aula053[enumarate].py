lista_nomes = ["Eduardo", "Theo", "Tatiana", "Claudio", "Maura"]

print(100 * "=")
print(f"lista de nomes: {lista_nomes}")
print(100 * "=")
print(f"nomes separados e por index:")
print(100 * "=")

for indice, nome in enumerate(lista_nomes):
    print(f"index {indice} | nome: {nome}")

print(100 * "=")