"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario_int = 0

print(100 * "=")

digitado = input("digite o horario em numero inteiro: ")

print(100 * "=")

try:
    horario_int = int(digitado)

    if horario_int >= 0 and horario_int <= 11:
        print(f"{horario_int} horas | Bom dia!")
    elif horario_int >= 12 and horario_int <= 17:
        print(f"{horario_int} horas | Boa tarde!")
    elif horario_int >= 18 and horario_int <= 23:
        print(f"{horario_int} horas | Boa noite!")
    else:
        print(f"{horario_int} | Horario invalido!!!")

except:
    print("Oque você digitou não é um numero inteiro!!")

print(100 * "=")