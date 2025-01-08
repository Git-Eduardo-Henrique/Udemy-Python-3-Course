num_1 = 0.1
num_2 = 0.7
soma = num_1 + num_2

print(100 * "=")
print(f"conta normal: {num_1} + {num_2} = {soma}")
print(f"formatação com f-string: {num_1} + {num_2} = {soma:.2f}")
print(f"usando round: {num_1} + {num_2} = {round(soma, 2)}")
print(100 * "=")