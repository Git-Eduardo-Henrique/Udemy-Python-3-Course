from os import system

palavra_secreta = "python"
letras_acertadas = ""
tentativas = 0

while True:
    palavra_formatada = ""

    print(100 * "=")
    digitado = input("digite uma letra da palavra secreta: ").lower()

    if len(digitado) > 1:
        print("Apenas uma letra!!!")
        continue

    tentativas += 1

    if digitado in palavra_secreta:
        letras_acertadas += digitado

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formatada += letra
        else:
            palavra_formatada += "*"

    if palavra_formatada == palavra_secreta:
        system("cls") # limpa o terminal

        print(100 * "=")
        print(f"Acertou tudo!! a palavra era: {palavra_secreta}")
        print(f"total de tentativas: {tentativas}")

        letras_acertadas = ""
        tentativas = 0
    else:
        print(f"palavra revelada: {palavra_formatada}")