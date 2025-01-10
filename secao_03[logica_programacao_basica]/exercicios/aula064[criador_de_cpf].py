from random import randint

soma_digito_1 = soma_digito_2 = digito_1 = 0
nove_digitos = ""

# GERAR 9 DIGITOS ALEATORIOS
for _ in range(9):
    nove_digitos += str(randint(0, 9))

# VERIFICAR PENULTIMO DIGITO

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

cpf_gerado = dez_digitos + str(digito_2)
cpf_gerado = f"{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:11]}"

print(100 * "=")
print(f"Nove digitos gerados: {nove_digitos} | dois ultimos digitos gerados: {digito_1},{digito_2}")
print(f"CPF gerado aleatoriamente: {cpf_gerado}")
print(100 * "=")
