# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def mult_nums(*nums):
    total = 1
    
    for num in nums:
        if num != 0:
            total *= num
    return total

def par_impar(num):
    if num % 2 == 0:
        return "PAR"

    return "IMPAR"

numeros_1 = 1, 2, 3, 4, 5, 6
numeros_2 = 0, 10, 2, 3, 0

conta_1 = mult_nums(*numeros_1)
conta_2 = mult_nums(*numeros_2)

print(100 * "=")
digitado = int(input("Digite o numero para verificar se é impar ou par: "))

veri_par_impar = par_impar(digitado)

print(100 * "=")
print(f"numeros conta 1: {numeros_1} | numeros conta 2: {numeros_2}")
print(100 * "=")
print(f"Valor da conta 1: {conta_1}\nValor da conta 2: {conta_2}")
print(100 * "=")

print(f"O numero {digitado} digitado é {veri_par_impar}!")
print(100 * "=")