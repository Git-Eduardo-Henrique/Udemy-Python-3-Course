import copy

# copy, sorted, produtos.sort
# Exercícios

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

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = copy.deepcopy(produtos)
novos_produtos = [
    {**prod, "preco": prod["preco"] * 1.1}
    for prod in novos_produtos
]

mostrar_produtos(novos_produtos, "Preços +10%")

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key=lambda item: item["nome"], reverse=True)

mostrar_produtos(produtos_ordenados_por_nome, "Ordenado por nome (decrescente)")

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(produtos_ordenados_por_preco, key=lambda item: item["preco"])

mostrar_produtos(produtos_ordenados_por_preco, "Ordenado por preço (crescente)")

print(100 * "=")