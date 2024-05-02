# A principal funcao de uma lambda é realizar um comando rapido em poucas linhas
funcao = lambda x,y: x+y

print(funcao(2,3))


# Exemplo de uso rapido para a função lambda
lista = [
    ['Produto 1', 43],
    ['Produto 2', 13],
    ['Produto 3', 67],
    ['Produto 4', 3],
    ['Produto 5', 4]
]

print(lista)
print() # Espaço em branco


lista.sort(key=lambda listas_inteiores: listas_inteiores[1])

print(lista)
