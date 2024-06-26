# Exercício - sistema de perguntas e respostas

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
    }
]

def conferindoResposta(resposta, questao):
    if (resposta == questao['Resposta']):
        return 'Você acertou'
    return 'Você errou'

for questao in perguntas:
    for chave, valor in questao.items():
        if chave == 'Pergunta':
            print(valor)
            
        if chave == 'Opções':
            for alternativas in valor:
                print(alternativas)

            resposta = input('Qual a resposta? ')

            print(conferindoResposta(resposta, questao))