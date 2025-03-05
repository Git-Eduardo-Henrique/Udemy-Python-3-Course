def concatenar(str):
    str_final = str

    def func_interna(concatenar=""):
        # pega a função na outra função
        nonlocal str_final
        str_final += concatenar
        return str_final
    
    return func_interna

conc = concatenar("A-")

print(100 * "=")
print(conc("B"))
print(conc("C"))
print(conc("D"))
print(100 * "=")