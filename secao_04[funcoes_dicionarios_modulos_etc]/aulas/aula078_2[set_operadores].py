set_1 = {1, 2, 3}
set_2 = {4, 2, 3}

print(100 * "=")
print(f"set 1: {set_1} | set 2: {set_2}")
print(100 * "=")

set_3 = set_1 | set_2 # uni dois sets 

print(f"set 3 unindo os dois sets: {set_3}")

set_3 = set_1 & set_2 # copia apenas os itens presentes em ambos os sets

print(f"set 3 com intersecção: {set_3}")

set_3 = set_1 - set_2 # mostra a item presente apenas no da esquerda

print(f"set 3 na diferenca: {set_3}")

set_3 = set_1 ^ set_2 # mostra a item presente apenas em cada um

print(f"set 3 na diferenca simetrica: {set_3}")

print(100 * "=")