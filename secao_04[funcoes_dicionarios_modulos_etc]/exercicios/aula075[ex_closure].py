def multiplicador(mult=1):

    def retornar_mult(num=0):
        return num * mult
    
    return retornar_mult

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

num_1 = 4
num_2 = 6
num_3 = 9

print(100 * "=")
print(f"{num_1} | {num_2} | {num_3} seram duplicados:")
print(f"Resultados: {duplicar(num_1)} | {duplicar(num_2)} | {duplicar(num_3)}")
print(100 * "=")

print(f"{num_1} | {num_2} | {num_3} seram triplicados:")
print(f"Resultados: {triplicar(num_1)} | {triplicar(num_2)} | {triplicar(num_3)}")

print(100 * "=")
print(f"{num_1} | {num_2} | {num_3} seram quadruplicados:")
print(f"Resultados: {quadruplicar(num_1)} | {quadruplicar(num_2)} | {quadruplicar(num_3)}")
print(100 * "=")