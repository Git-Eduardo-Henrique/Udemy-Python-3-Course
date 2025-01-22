def executar(funcao, *args):
    return funcao(*args)

print(100 * "=")

# função de somar dois numeros
print(executar(lambda x, y: x + y, 2, 2))

# função lambda com outra lambda ( multiplicar numeros )
duplicar = executar(
    lambda m: lambda n: n * m, 2
)

print(duplicar(3))

print(100 * "=")