from itertools import groupby

def ordenar_p_nota(aluno):
    return aluno["nota"]

def mostrar_grupos(grupos):
    for chave, grupo in grupos:
        print(100 * "=")
        print(f"Alunos no grupo de nota: {chave}")
        print(100 * "=")
        for aluno in grupo:
            print(aluno)

alunos = [
     {'nome': 'Luiz', 'nota': 'A'},
     {'nome': 'Letícia', 'nota': 'B'},
     {'nome': 'Fabrício', 'nota': 'A'},
     {'nome': 'Rosemary', 'nota': 'C'},
     {'nome': 'Joana', 'nota': 'D'},
     {'nome': 'João', 'nota': 'A'},
     {'nome': 'Eduardo', 'nota': 'B'},
     {'nome': 'André', 'nota': 'A'},
     {'nome': 'Anderson', 'nota': 'C'},
 ]

alunos_ordenados = sorted(alunos, key=ordenar_p_nota) # ordena alunos por nota
# ira separar os alunos por categoria em cada nota
grupos_p_nota = groupby(alunos_ordenados, key=ordenar_p_nota)

mostrar_grupos(grupos_p_nota)
print(100 * "=")