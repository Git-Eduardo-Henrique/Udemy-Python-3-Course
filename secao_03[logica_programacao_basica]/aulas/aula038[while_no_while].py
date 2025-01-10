linha = 0

print(100 * "=")
print("5 linhas com 5 colunas")

while linha < 5:
    linha += 1
    coluna = 0

    print(100 * "=")

    while coluna < 5:
        coluna += 1
        print(f"{linha} | {coluna}")
 
print(100 * "=")