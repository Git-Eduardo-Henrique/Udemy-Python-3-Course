from itertools import count

# funciona como um range, pode receber inicio e passo mas não tem fim
contador = count()

print(100 * "=")
print("inicio do contador até 100")

for i in contador:
    if i > 100: # sem isso ele iria contar infinitamente
        break

    print(i)
print(100 * "=")