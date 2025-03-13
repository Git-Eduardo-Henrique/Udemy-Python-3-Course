from functools import partial

def mostrar_produtos(lista_produtos, msg=""):
    print(100 * "=")
    print(f"mostrando lista: {msg}")
    for produto in lista_produtos:
        print(f"{produto["nome"]} | R${produto["preco"]:.2f}") 

def aumentar_porc(valor, porc):
    return round(valor * porc, 2)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

mostrar_produtos(produtos, "Original")

# permite guardar apenas um argumento de uma função, nesse caso posso usar para aumentar
# qualquer valor em 10%
aumenta_dez_porc = partial(
    aumentar_porc,
    porc=1.1
)

novos_produtos = [
    {**produto, "preco": aumenta_dez_porc(produto["preco"])}
    for produto in produtos
]

mostrar_produtos(novos_produtos, "Aumentado em 10%")
print(100 * "=")






