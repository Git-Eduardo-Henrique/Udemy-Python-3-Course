def lock_func(func):

    def inter_func(arg):

        is_string(arg)
        print("função decorada")

        return func(arg)
    
    return inter_func

def is_string(param):
    if not isinstance(param, str):
        raise TypeError("Seu parametro não é uma string")

# ira executar essa função passando como parametro a função invert_string
@lock_func
def invert_string(str):
    return str[::-1]

print(100 * "=")
print(invert_string("Python"))
print(100 * "=")