from itertools import combinations, permutations, product

def show_lists(lista, msg=""):
    print(100 * "=")
    print(f"Mostrando lista: {msg}")
    for item in lista:
        print(f"{item[0]} | {item[1]}")

pessoas = [
    "Eduardo", "Theo", "Tatiana", "Claudio"
]

camisas = [
    ["Preta", "Branca"],
    ["P", "M", "G"]
]

print(100 * "=")
print(f"Lista pessoas = {pessoas}")
print(f"Lista camisas = {camisas}")

# cria grupos de dois na lista sem repetir possibilidades
show_lists(list(combinations(pessoas, 2)), "COMBINATIONS | PESSOAS")
# cria grupos de dois na lista repetindo possibilidades
show_lists(list(permutations(pessoas, 2)), "PERMUTATIONS | PESSOAS")
# junta todas as possibilidades da lista camisas
show_lists(list(product(*camisas)), "PRODUCT | CAMISAS")

print(100 * "=")