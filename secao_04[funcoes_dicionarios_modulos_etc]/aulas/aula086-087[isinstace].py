def verificar_tipo(lista, tipo):
    print(100 * "=")
    print(f"Verificando tipo: {tipo}")
    print(100 * "=")

    for item in lista:
        # retorna true caso o valor for do mesmo tipo
        # ex: isinstance("string", str):
        if isinstance(item, tipo):
            print(f"{item} é do tipo: {tipo}")


lista_coisas = [1, 2, 3, 4.5, "string 1", "nome top", True, False, {"nome": "Eduardo"}]

# para verificar dois tipos é só enviar uma tupla: (int, float)
verificar_tipo(lista_coisas, int)
verificar_tipo(lista_coisas, float)
verificar_tipo(lista_coisas, str)
verificar_tipo(lista_coisas, bool)
verificar_tipo(lista_coisas, dict)

print(100 * "=")
