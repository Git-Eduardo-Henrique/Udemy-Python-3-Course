resultado = 0

while True:
    print(100 * "=")

    try:
        num_1 = float(input("digite o primeiro numero: "))
        num_2 = float(input("digite o segundo numero: "))

    except:
        print(100 * "=")
        print("Algum dos numeros não são validos!!")
        continue

    operador = input("digite o operador (+ - * /): ")

    print(100 * "=")

    if operador in "+-*/" and len(operador) <= 1:
        if operador == "+":
            resultado = num_1 + num_2
        elif operador == "-":
            resultado = num_1 - num_2
        elif operador == "*":
            resultado = num_1 * num_2
        elif operador == "/":
            resultado = num_1 / num_2

        print(f"{num_1:.2f} {operador} {num_2:.2f} = {resultado:.2f}")
    else:
        print("seu operador é inválido!")
        continue
    
    print(100 * "=")
    sair = input("deseja sair? [s]=sim: ").lower().startswith("s")

    if sair:
        break

print(100 * "=")