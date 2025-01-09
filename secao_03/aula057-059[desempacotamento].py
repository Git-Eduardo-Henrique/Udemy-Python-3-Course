texto = "Texto top"

lista_nomes = [
    ["Eduardo", "Theo"], 
    ["Claudio", "Tatiana"], 
    ["Erick", "Julia"]
    ]

print(100 * "=")

print(f"string normal: {texto} | desempacotada:", *texto)
print(f"lista normal: {lista_nomes}")

print(100 * "=")
print("desempacotadas:")
print(*lista_nomes, sep="\n")
print(100 * "=")