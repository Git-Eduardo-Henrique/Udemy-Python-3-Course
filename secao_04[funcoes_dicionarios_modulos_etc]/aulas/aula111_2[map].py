lista_nums = [1, 2, 3, 4, 5, 6]

# recebe uma função e os parametros que seram passados na função
multiplica_3 = map(
    lambda x: x *3,
    lista_nums # cada valor da lista será passado para a função, "x"
)

novos_nums = list(multiplica_3)

print(100 * "=")
print(f"lista original: {lista_nums}\nApós map para multiplicar por 3: {novos_nums}")
print(100 * "=")