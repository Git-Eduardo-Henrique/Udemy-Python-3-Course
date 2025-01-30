def check_nums(num):
    if not isinstance(num, (int, float)):
        tipo_num = type(num)

        # raise = levantar erros com mensagem personalizada
        # __name__ = pegar apenas o nome da classe
        raise TypeError(f"'{num}' não é um valor inteiro ou flutuante | {tipo_num.__name__} enviado")


def dividir(num1, num2):
    check_nums(num1)
    check_nums(num2)
    return num1 / num2

print(100 * "=")
print(dividir(24, 2))
print(100 * "=")
print(dividir(2, ""))
print(100 * "=")
