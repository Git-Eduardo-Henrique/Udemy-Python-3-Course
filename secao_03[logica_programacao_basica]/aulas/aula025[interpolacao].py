print(100 * "=")

nome = input("digite seu nome: ")
dindin = int(input("quanto dinheiro voce tem: "))

# f string mil vezes pior
# %s = strings
# %i = inteiro
# %x = hexadecimal
print(100 * "=")
print("%s tem R$ %i" % (nome, dindin))
print("Hexadecimal de %i: %08x" % (dindin, dindin))

print(100 * "=")