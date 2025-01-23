produtos = [
    {"nome": "Toddinho", "preco": 4.5},
    {"nome": "Panela", "preco": 35},
    {"nome": "Iphome 19", "preco": 7999}
]

# ira copiar cada dicionario para a lista aumentando o preco dos produtos
novos_precos = [
    {**produto, "preco": produto["preco"] * 1.5} # oque sera retornado
    if produto["preco"] < 50 else {**produto} # mapeamento
    for produto in produtos
]

print(100 * "=")
print(f"Produtos antigo: {produtos}\nNovos produtos: {novos_precos}")
print(100 * "=")

# cada for a baixo sera dentro do for acima
lista_nums = [
    (x, y, z)
    for x in range(3)
    for y in range(3)
    for z in range(3)
]

print(lista_nums)