from copy import deepcopy

dic_1 = {
    "chave_1" : 1,
    "chave_2" : 2,
    "lista" : [0, 1, 2, 3]
}

# .copy() = faz uma copia raza do dicionario, disvincula apenas não imutaveis
dic_2 = dic_1.copy()
dic_2["chave_1"] = 10
dic_2["lista"][0] = 999

print(100 * "=")
print(f"Dicionario original: {dic_1}\nNovo dicionario com Shallow copy: {dic_2}")

# deepcopy() = faz uma copia completa disvinculando tudo
dic_3 = deepcopy(dic_1)
dic_3["lista"][0] = 555

print(100 * "=")
print(f"Dicionario original: {dic_1}\nNovo dicionario com Deep copy: {dic_3}")

print(100 * "=")