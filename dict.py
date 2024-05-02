def detalharDict(dicionario):
    for chave, valor in dicionario.items():
        print(chave + ' ' + valor)
    print()

#Criando um dict
pessoa = { #Ou "pessoa = dict()"
    'nome':'Kaiky',
    'Sobrenome':'Bitencourt',
    'Idade':'18',
    'altura':'1.75'
}

print(pessoa['nome'])
print()

detalharDict(pessoa)

#Adicionando valores
pessoa['Nascimento'] = '2003'
detalharDict(pessoa)

#Apagando chaves
del pessoa['Sobrenome']

#Conferindo se a chave foi deletada
if (pessoa.get('Sobrenome') is None):
    print('Não existe')
else:
    print(pessoa['Sobrenome'])

#Retornando quantas chaves existem no dict
print(len(pessoa))

#Retornando as chaves
print(pessoa.keys()) #Pode ser convertido para list ou tuple

#Retornando os valores das chaves
print(pessoa.values()) #Pode ser convertido para list ou tuple

#Retornando as chaves seguidas dos valores delas
print(pessoa.items()) #Pode ser convertido para list ou tuple

#Deleta uma chave, porém retorna ela
deletado = pessoa.pop('Nascimento')
print(deletado)

#Deleta o ultimo item e retorna ele
deletado = pessoa.popitem()
print(deletado)

#Definindo o valor de uma chave caso ela esteja vazia
print(pessoa.setdefault('pai', 'Helio'))
detalharDict(pessoa)

#Adicionando listas ao diciorio
pessoa['Irmaos'] = ['Paulo', 'Gabriel']
print(pessoa)

    # Formas de copiar uma lista
# Apenas faz com que os dois dicionario indiquem o mesmo local na memoria, qualquer mudança em um ocorrerá também no outro
pessoa01 = pessoa

# Realizará uma copia de um dicionario para o outro, e mudanças em um não ocorreram no outro, a não ser que o dicionario possua uma lista, qualquer mudança nessa lista ocorrera na lista do outro dicionario, porquê ambas indicam o mesmo local na memoria
pessoa02 = pessoa.copy() #Copia rasa (Shallow Copy)

# Realizará uma copia total, qualquer mudança não afetará sua copia
import copy

pessoa03 = copy.deepcopy(pessoa)

# Dando um update mais geral para o dicionario
pessoa.update({
    'nome' : 'Batman',
    'Idade' : '10000',
    'pai' : 'Thomas',
    'Irmaos' : 'nenhum'
})

detalharDict(pessoa)