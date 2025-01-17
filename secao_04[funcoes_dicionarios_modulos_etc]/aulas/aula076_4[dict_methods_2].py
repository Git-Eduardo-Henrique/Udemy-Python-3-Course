pessoa = {
    "Nome" : "Eduardo",
    "Sobrenome" : "Henrique",
    "Idade" : 20
}

print(100 * "=")
print(f"Dicionario: {pessoa}")
print(100 * "=")

# remove um valor do dicionario porem retorna o valor removido
nome_removido = pessoa.pop("Sobrenome")

print(f"Sobrenome removido com POP: {nome_removido}")
print(f"Dicionario após: {pessoa}")
print(100 * "=")

# remove o ultimo valor
pessoa.popitem()

print(f"Dicionario após POP ITEM: {pessoa}")
print(100 * "=")

# update = permite atualizar dados e criar novas chaves ao mesmo tempo
pessoa.update({
    "Nome" : "Roberto",
    "Sobrenome" : "Carlos",
    "Idade" : 20
})

print(f"Dicionario após UPDATE: {pessoa}")
print(100 * "=")