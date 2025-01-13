x = 0

def linha():
    print(100 * "=")

def multi(y=2):
    # transforma uma variavel da função em global
    global x
    x = 10

    print(f"{x} + {y} = {x + y}")

linha()
print(f"x antes: {x}")
multi(y=4)
print(f"x agora: {x}")
linha()