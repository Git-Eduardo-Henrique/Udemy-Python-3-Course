pessoa = {
    "nome": "Eduardo",
    "sobrenome": "Henrique"
}

nova_chave = "idade"
pessoa[nova_chave] = 20

print(100 * "=")
print(f"adicionando chave: {pessoa}")

# deleta uma chave no dicionario
del pessoa["sobrenome"]

print(100 * "=")
print(f"após del em sobrenome: {pessoa}")

print(100 * "=")
print(f"verificando valor:")

# get = retorna o valor caso a chave exista e None caso não
if pessoa.get("sobrenome") is not None:
    print(f"Valor existe! {pessoa['sobrenome']}")
else:
    print("Valor não existe!!!")

print(100 * "=")
print("Mostrando lista com for: ")

for chave in pessoa:
    print(f"{chave} | {pessoa[chave]}")

print(100 * "=")