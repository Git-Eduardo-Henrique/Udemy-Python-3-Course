lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir_lista(lista):
    print(100 * "=")

    for item in lista:
        print(item)

# sorted(lista para ordenar, key=parametro para ordenar)
# lambda = função | item = argumento | : oque ira retornar
lista_nome = sorted(lista, key=lambda item: item["nome"]) # ira ordenar pelo nome
lista_s_nome = sorted(lista, key=lambda item: item["sobrenome"])

exibir_lista(lista_nome)
exibir_lista(lista_s_nome)
print(100 * "=")
