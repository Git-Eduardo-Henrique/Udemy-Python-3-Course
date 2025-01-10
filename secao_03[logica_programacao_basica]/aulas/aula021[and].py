senha = "Batata_Frita"

print(100 * "=")

entrada = input("E = Entrar | Outro = Sair: ")
senha_digitada = input("digite sua senha: ")

print(100 * "=")

# and = verifica se duas ou mais expressões são verdadeiras
if entrada == "E" and senha_digitada == senha:
    print("Senha correta! entrando no sistema...")
else:
    print("Senha errada ou saindo do sistema...")

print(100 * "=")