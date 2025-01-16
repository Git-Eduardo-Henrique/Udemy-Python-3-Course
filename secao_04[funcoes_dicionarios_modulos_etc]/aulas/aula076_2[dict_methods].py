pessoa = {
    "nome": "Eduardo",
    "sobrenome": "Henrique",
    "idade": 20,
}


print(100 * "=")
print(f"dicionario: {pessoa}")

# len = igual ao das listas, mostra quantas chaves tem
print(f"tamanho do dicionario: {len(pessoa)}")

print(100 * "=")
print("mostrando as chaves:")
for key in pessoa.keys():
    print(key)

print(100 * "=")
print("mostrando os valores:")
for value in pessoa.values():
    print(value)

print(100 * "=")
print("mostrando ambos:")
for chave, valor in pessoa.items():
    print(f"{chave} | {valor}")

# caso o valor não exista ele irá colocar um valor padrão
pessoa.setdefault("Altura", 1.8)
print(100 * "=")
print(f"nova lista após setdefault: {pessoa}")

print(100 * "=")