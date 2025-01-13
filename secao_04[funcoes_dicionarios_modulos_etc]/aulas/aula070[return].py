def linha():
    print(100 * "=")

def somar(x, y):
    # rotorna valores aonde quiser ( sem = None )
    return x + y

linha()
soma1 = somar(10, 20)
soma2 = somar(30, 10)
print(f"{soma1} + {soma2} = {soma1 + soma2}")
linha()