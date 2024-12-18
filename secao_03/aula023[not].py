senha = "senha_top"

print(100 * "=")

senha_digitada = input("digite sua senha: ")

print(100 * "=")

# not = troca o valor (True vira False e False vira True)
if not senha_digitada:
    print("você não digitou nada!")
else:
    if senha == senha_digitada:
        print("Senha Correta!")
    else:
        print("Senha incorreta!")

print(100 * "=")