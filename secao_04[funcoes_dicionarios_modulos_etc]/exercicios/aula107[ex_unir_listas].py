# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(list1=[], list2=[]):
    # calcula a lista com menos indices
    menor = min((len(list1), len(list2)))

    return [
        (lista1[i], lista2[i])
        for i in range(menor)
    ]

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

lista_unida = zipper(lista1, lista2)

print(100 * "=")
print(f"Lista 1: {lista1} | Lista 2: {lista2}")
print(f"Nova lista unida: {lista_unida}")
print(100 * "=")