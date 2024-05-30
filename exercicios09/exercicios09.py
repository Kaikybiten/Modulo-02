import json
import os

with open('exercicios09\\tarefas.json', 'r') as listaDeTarefasJson:
    listaDeTarefas = json.load(listaDeTarefasJson)

sair = False
opcao = None
deletados = []

def tratandoOpcao(opcao):
    if (not(opcao.isalpha())):
        return opcao
    return opcao.lower()

def desfazer():
    if (listaDeTarefas):
        item = listaDeTarefas.pop()
        deletados.append(item)
        return 1
    print()
    print('Não há itens na lista')
    print()

def refazer():
    if (deletados):
        item = deletados.pop()
        listaDeTarefas.append(item)
        return 1
    print()
    print('Você não apagou nenhum item')
    print()
    return 1

def listar():
    if (not(listaDeTarefas)):
        print()
        print('Não há itens na lista')
        print()
        return 1
    print()
    for x in listaDeTarefas:
        print(x)
    print()
    return 1

while (opcao!= 'sair'):
    opcao = input(
        '\nDigite o item que deseja adicionar a lista de tarefa\nOu digite o comando que desejar realizar\nlistar, desfazer, refazer ou sair:\n'
    )

    opcao = tratandoOpcao(opcao)

    if (opcao == 'listar'):
        listar()
    elif (opcao == 'desfazer'):
        desfazer()
    elif (opcao == 'refazer'):
        refazer()
    elif (opcao == 'sair'):
        break
    elif (opcao == 'cls'):
        os.system('cls')
        continue
    else:
        listaDeTarefas.append(opcao)
    
with open('exercicios09\\tarefas.json', 'w') as listaDeTarefasJson:
    json.dump(
        listaDeTarefas, listaDeTarefasJson
    )