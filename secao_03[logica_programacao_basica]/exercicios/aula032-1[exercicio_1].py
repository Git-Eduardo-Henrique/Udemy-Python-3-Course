"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = 0

print(100 * "=")

digitado = input("digite um numero inteiro: ")

print(100 * "=")

if digitado.isdigit():
    numero = int(digitado)

    if numero % 2 == 0:
        print(f"{numero} é um numero PAR")
    else:
        print(f"{numero} é um numero ÍMPAR")
else:
    print(f"'{digitado}' não é um numero inteiro!")

print(100 * "=")