frase = "olha só que, coisa legal"
lista_palavras = frase.split() # sepera por espaços caso não explicificar
lista_frases = frase.split(",") # agora separa por ","

print(100 * "=")

print(f"frase original: {frase}\npalavras separadas: {lista_palavras}")
print(f"frases separadaS: {lista_frases}\nRemovendo os espaços: ")

for i, _ in enumerate(lista_frases):
    print(lista_frases[i].strip()) # strip = remove os espaços no começo e final

print(100 * "=")