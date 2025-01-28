lista_top = ["Valor_1", "Valor_2", "Valor_3"]

iteravel = iter(lista_top) # entrega um valor de cada vez

print(100 * "=")
print(lista_top)
print(next(iteravel)) # entrega o proximo valor
print(next(iteravel))
print(next(iteravel))
# tentar next após isso daria StopInteration
print(100 * "=")

# não é uma tupla, ele não salva os valores na memoria, apenas sabe o proximo valor
generator = (num for num in range(100)) 

print(next(generator))
print(next(generator))
print(next(generator))
print(100 * "=")