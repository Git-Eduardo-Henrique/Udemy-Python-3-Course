

print(100 * "=")

primeiro_valor = input("digite o primeiro valor: ")
segundo_valor = input("digite o segundo valor: ")

print(100 * "=")

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} é maior do que {segundo_valor=}")
elif primeiro_valor == segundo_valor:
    print(f"os valores são iguais: {primeiro_valor}")
else:
    print(f"{segundo_valor=} é maior do que {primeiro_valor=}")

print(100 * "=")