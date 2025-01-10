"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print(100 * "=")

nome = input("digite seu primeiro nome: ")
tam_nome = len(nome)

print(100 * "=")

if tam_nome > 1:
    if tam_nome <= 4:
        print(f"{nome} é um nome curto!")
    elif tam_nome <= 6:
        print(f"{nome} é um nome de tamanho normal!")
    else:
        print(f"{nome} é um nome bem grande!")
else:
    print("digite pelo menos 2 caractheres!")

print(100 * "=")