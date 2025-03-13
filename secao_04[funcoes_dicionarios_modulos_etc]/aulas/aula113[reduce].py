from functools import reduce

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

# ira fazer o somatorio de todos os precos da lista produtos
# recebe uma função com dois valores
total_preco = reduce(
    lambda total, produto: total + produto["preco"],
    produtos,
    0 # valor inicial do total
)

print(100 * "=")
print(f"o valor total da compra é R${round(total_preco, 2)}")
print(100 * "=")