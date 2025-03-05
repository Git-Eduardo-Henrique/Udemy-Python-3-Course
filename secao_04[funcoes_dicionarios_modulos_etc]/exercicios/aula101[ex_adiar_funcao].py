# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x):
    def func_interna(y):
        return funcao(x, y)
    return func_interna

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(100 * "=")
print(f"função de somar 4 com 5: {soma_com_cinco(4)}")
print(f"função de multiplicar 5 com 10: {multiplica_por_dez(5)}")
print(100 * "=")