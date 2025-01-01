contador = maior_numero = letra_aparecoes = 0
letra = letra_mais_apareceu = ""

print(100 * "=")

digitado = input("digite alguma coisa para ver a letra que mais apareceu: ").upper()

print(100 * "=")

while contador < len(digitado):
    letra = digitado[contador]

    contador += 1

    if letra == " ":
        continue

    letra_aparecoes = digitado.count(letra)
    
    if letra_aparecoes > maior_numero:
        letra_mais_apareceu = letra
        maior_numero = letra_aparecoes

print(f"letra que mais apareceu na frase foi '{letra_mais_apareceu}' que apareceu {maior_numero} vezes")
print(100 * "=")