senha = "Batata_Frita"

print(100 * "=")

entrada = input("E = Entrar | Outro = Sair: ")

print(100 * "=")

# or = verifica alguma das expressões é verdadeiro
if entrada == "E" or entrada == "e": 

    senha_digitada = input("digite sua senha: ")

    if senha_digitada == senha:
        print("Senha correta! entrando no sistema...")
    else:
        print("Senha incorreta!")

else:
    print("Saindo do sistema...")

print(100 * "=")