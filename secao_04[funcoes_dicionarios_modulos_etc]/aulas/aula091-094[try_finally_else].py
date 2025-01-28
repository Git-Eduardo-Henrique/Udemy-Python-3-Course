try:
    print(100 * "=")
    num_1 = int(input("digite um numero: "))
    num_2 = int(input("digite um numero: "))
    print(100 * "=")

    conta = num_1 / num_2
    print(f"{num_1} / {num_2} = {conta:.2f}")
    
except ValueError:
    print(100 * "=")
    print("Algum dos valores não é um NUMERO INTEIRO!!")

except ZeroDivisionError:
    print("Impossivel dividir por ZERO!!")

except Exception as error: # para qualquer outro erro
    print(f"ERRO: {error.__class__.__name__}") # mostra o erro
    print(f"MSG: {error}") # mostra a mensagem de erro

else: # apenas se não ouver erros
    print("Conta realizada sem erros!!!")

finally: # executa mesmo com erros / bom para sempre fechar arquivos futuramente
    print(100 * "=")
    print("FECHAR ARQUIVO!")

print(100 * "=")
