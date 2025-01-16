def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    
    # ira retornar a funcao sem executa / guardar os valores enviados na memoria
    return saudar

bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")

print(100 * "=")
# função interna só executa agora
print(f"{bom_dia("Eduardo")}\n{bom_dia("Tatiana")}")
print(f"{boa_noite("Theo")}\n{boa_noite("Claudio")}")
print(100 * "=")