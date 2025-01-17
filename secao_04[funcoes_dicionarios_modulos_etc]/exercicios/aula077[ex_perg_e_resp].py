from os import system

# Exercício - sistema de perguntas e respostas
acertos = 0

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for index, pergunta in enumerate(perguntas):
    print(100 * "=")
    print(f"Pergunta {index+1} | {pergunta["Pergunta"]}")
    print(100 * "=")

    print(f"Opções:")
    
    for i, opt in enumerate(pergunta["Opções"]):
        print(f"{i}) {opt}")

    print(100 * "=")

    resp = input("Sua opção: ")

    system("cls")

    if resp.isdigit():
        resp = int(resp)
    else:
        resp = None

    if resp is not None:
        if resp >= 0 and resp < len(pergunta['Opções']):
            if pergunta["Opções"][resp] == pergunta["Resposta"]:
                acertos += 1
                print("Resposta correta ✅✅")
                continue
    
    print("Resposta incorreta ❌❌")

print(100 * "=")
print(f"Você acertou {acertos} de {len(perguntas)} perguntas!!")
print(100 * "=")