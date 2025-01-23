def mostra_args(*args, **kwargs):
    print(f"Argumentos não nomeados: {args}\nArgumentos nomeados:")

    for key, item in kwargs.items():
        print(f"chave: {key} | item: {item}")

nome_pessoa = {
    "Nome": "Eduardo",
    "Sobrenome": "Henrique"
}

dados_pessoa = {
    "Idade": 20,
    "Altura": 1.8
}

# empacota os dados no novo dicionario
pessoa = {**nome_pessoa, **dados_pessoa}

print(100 * "=")
print(f"dicionario de nome: {nome_pessoa}\ndicionario de outros: {dados_pessoa}")
print(f"dicionario novo: {pessoa}")
print(100 * "=")

# os não nomeados vão para o *args e nomeados para os *kwargs
# **dict desempacota os argumentos
mostra_args(2, 3, 4, 5, **pessoa)
print(100 * "=")
