# set = {}, set() | elimina itens duplicados | não garante a ordem
nums = [1, 2, 3, 3, 3, 3, 4, 4, 4]
set_1 = set(nums) # não recebe mutaveis [], {} e etc

print(100 * "=")
print(f"lista normal: {nums}\ncom set: {set_1}")
print(100 * "=")

set_1.add(5) # só aceita um valor
set_1.update(("Olá mundão", 5, 6, 7)) # () para adicionar mais valores e strings

print(f"após add e update: {set_1}")
print(100 * "=")

set_1.discard("Olá mundão") # não recebe index

print(f"após discard: {set_1}")
print(100 * "=")

set_1.clear() # remove tudo

print(f"após clear: {set_1}")
print(100 * "=")