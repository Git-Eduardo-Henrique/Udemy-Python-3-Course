print(100 * "=")

nome = input("digite seu nome: ")
idade = input("digite sua idade: ")

print(100 * "=")

if nome and idade:

    print(f"seu nome: {nome} | sua idade: {idade}")
    print(f"sua nome invertido: {nome[::-1]}")

    if " " in nome:
        print("seu nome tem 1 ou mais espacos")
    else:
        print("seu nome nao tem espacos")

    print(f"seu nome tem {len(nome)} letras")
    print(f"a primeira letra do seu nome: {nome[0]}")
    print(f"a primeira letra do seu nome: {nome[-1]}")
else:
    print("voce nao digitou algum dos campos")

print(100 * "=")