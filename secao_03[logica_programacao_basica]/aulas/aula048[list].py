lista_top = ["Eduardo", 123, 456, True]

print(100 * "=")
print(f"lista original: {lista_top}")
print(100 * "=")

lista_top[3] = 789 # muda o valor
del lista_top[0] # deleta o primeiro valor

lista_top.append("novo valor") # adiciona um valor

print(f"lista após del, append e mudança de valor: {lista_top}")
print(100 * "=")

lista_top.pop() # deleta o ultimo valor
lista_top.insert(1, 100) # muda o valor de um index (index, valor)

print(f"lista pop e insert: {lista_top}")
print(100 * "=")

outra_lista = lista_top.copy() # copia os valores para outra lista
outra_lista.extend(lista_top) # adiciona os valores da lista (neste caso vai estar duplicado)

print(f"nova lista após copy e extend: {outra_lista}")
print(100 * "=")