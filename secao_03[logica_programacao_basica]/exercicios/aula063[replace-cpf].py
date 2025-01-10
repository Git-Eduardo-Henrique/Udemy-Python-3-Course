soma_digito_1 = soma_digito_2 = digito_1 = 0

print(100 * "=")
# replace = troca um valor por outro na string
cpf = input("Digite o cpf para ser validado: ").replace(".", "").replace("-", "")
print(100 * "=")

# VERIFICAR NUMEROS REPETIDOS
digito_1_rep = cpf[0] * len(cpf) # Ex: 01234 retorna 00000

if cpf == digito_1_rep:
    print("CPF COM NUMEROS REPETIDOS!!! INVALIDO!!")

else:
    # VERIFICAR PENULTIMO DIGITO
    nove_digitos = cpf[:9]
    multiplicador = 10

    for digito in nove_digitos:
        soma_digito_1 += int(digito) * multiplicador
        multiplicador -= 1

    digito_1 = (soma_digito_1 * 10) % 11

    digito_1 = digito_1 if digito_1 <= 9 else 0

    # VERIFICAR ULTIMO DIGITO
    dez_digitos = nove_digitos + str(digito_1)
    multiplicador = 11

    for digito in dez_digitos:
        soma_digito_2 += int(digito) * multiplicador
        multiplicador -= 1

    digito_2 = (soma_digito_2 * 10) % 11

    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_valido = dez_digitos + str(digito_2)

    print(f"Cpf Digitado: {cpf}")
    print(f"Penultimo e ultimo digitos para os 9 primeiros digitos: {digito_1} | {digito_2}")
    print(100 * "=")

    if cpf_valido == cpf:
        print("O CPF DIGITADO É VÁLIDO!!!")
    else:
        print("O CPF DIGITADO É INVÁLIDO!!!")

print(100 * "=")