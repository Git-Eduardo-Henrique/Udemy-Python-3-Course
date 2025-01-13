def linha():
    print(100 * "=")

def somar(x, y, z=None):
    if z is None:
        print(f"{x} + {y} = {x + y}")
    else:
        print(f"{x} + {y} + {z} = {x + y + z}")

linha()
somar(10, 3)
somar(y=23, x=90)
somar(10, 3, 2)
somar(z=23, y=87, x=100)
linha()