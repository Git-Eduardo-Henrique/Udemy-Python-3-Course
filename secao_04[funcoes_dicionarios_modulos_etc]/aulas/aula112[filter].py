def mostrar_produtos(lista_produtos, msg=""):
    print(100 * "=")
    print(f"mostrando lista: {msg}")
    for produto in lista_produtos:
        print(f"{produto["nome"]} | R${produto["preco"]:.2f}") 

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

mostrar_produtos(produtos, "Original")

# ira retornar apenas os produtos com mais de 20 no preço
# a função executara em cada item da lista
novos_produtos = filter(
    lambda produto: produto["preco"] > 20,
    produtos
)

mostrar_produtos(novos_produtos, "Acima de 20 reais")
print(100 * "=")