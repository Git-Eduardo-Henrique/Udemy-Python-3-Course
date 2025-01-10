from os import system

textos = ("Loja do Jubileu ( você não sabe nem eu )", \
          "[L] = Listar | [I] = Inserir item | [A] = Apagar item | [S] = Sair")

lista_compras = []

while True:
    print(100 * "=")
    print(textos[0].center(100))
    print(100 * "=")
    print(textos[1].center(100))
    print(100 * "=")

    entrada = input("sua opção: ").lower()

    system("cls") # limpa o terminal
    print(100 * "=")

    if entrada and entrada in "lias":

        if entrada == "s":
            break

        elif entrada == "l":

            if lista_compras:
                for indice, nome in enumerate(lista_compras):
                    print(f"{indice} | {nome}")
            else:
                print(f"A sua lista de compras está vazia!!!")

        elif entrada == "i":

            nome_item = input("nome do item: ").upper()
            lista_compras.append(nome_item)

            print(f"{nome_item} adicionado a lista!!!")

        elif entrada == "a":

            tam_lista = len(lista_compras)

            try:
                indice_digitado = int(input(f"Indice do item a ser apagado [0 até {tam_lista - 1}]: "))
                del(lista_compras[indice_digitado])
            except ValueError:
                print("Isso não é um numero!!!")
            except IndexError:
                print("Índice Inválido!!!!")

    else:
        print("Opção Inválida!!!!")
