def linha():
    print(100 * "=")

# *variavel = permite enviar varios dados não nomeados para a função que acabam virando uma tupla
def somar(*args):
    soma = 0

    for num in args:
        soma += num

    return soma

linha()
print(f"Soma 1: {somar(2, 2, 3, 3, 4, 4, 5, 5)}")
print(f"Soma 2: {somar(2, 3, 4, 5)}")

# função pronta para soma ( recebe tuplas, listas e outros )
print(f"Soma 3: {sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))}")

linha()