"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

def mostrar_lista(lista, msg=""):
    print(100 * "=")
    print(f"mostrando lista: {msg}")
    for i, item in enumerate(lista):
        print(f"index {i} | {item}") 

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4, 5]

lista_soma = [
    x + y
    # retorna tupla unindos os indexes até o tamanho da lista menor
    for x, y in zip(lista_a, lista_b)
]

mostrar_lista(lista_a, "LISTA A")
mostrar_lista(lista_b, "LISTA B")
mostrar_lista(lista_soma, "LISTAS SOMADAS")
print(100 * "=")