soma_cpf = digito_1 = 0
multiplicador = 10

print(100 * "=")
cpf = input("digite o cpf para ser validado ( apenas numeros ): ")
nove_digitos = cpf[:9]
print(100 * "=")

""" Primeiro Digito do CPF
1° soma dos 9 primeiros dígitos do CPF multiplicando cada um 
dos valores por uma contagem regressiva começando de 10
2° Somar todos os resultados: 
Cpf Ex: 746.824.890-70
Ex: 70+36+48+56+12+20+32+27+0 = 301 """

for digito in nove_digitos:
    soma_cpf += int(digito) * multiplicador
    multiplicador -= 1

""" 3° Multiplicar o resultado anterior por 10
4° Obter o resto da divisão da conta anterior por 11 """

digito_1 = (soma_cpf * 10) % 11

""" 5° Se o resultado anterior for maior que 9: resultado é 0
contrário disso: resultado é o valor da conta """

digito_1 = digito_1 if digito_1 <= 9 else 0

if int(cpf[9]) == digito_1:
    print(f"penultimo digito é {digito_1} | Valido!!!")
else:
    print(f"penultimo digito deveria ser {digito_1} | INVALIDO!!!")

print(100 * "=")