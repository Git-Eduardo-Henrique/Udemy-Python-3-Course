print(100 * "=")

digitado = input("digite um numero: ")

print(100 * "=")

# testa se o codigo irá ou não gerar um erro

try:
    numero = float(digitado)
    print(f"o dobro de {numero:.2f} é {numero * 2:.2f}")
except:
    print(f"'{digitado}' não é um numero válido")

print(100 * "=")