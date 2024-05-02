# Ordenando os valores da lista
varLista03 = [7, 5, 2, 8, 0, 1, 4]
varLista03.sort()
print(varLista03)

varLista03 = [7, 5, 2, 8, 0, 1, 4]
varLista03.sort(reverse=True)
print(varLista03)

# Ordenando um dicionario
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#Lambda é uma função sem nome, apenas argumentos e um return, neste caso, "item" representa cada
#dicionário individual dentro da lista. A expressão "item['nome'] acessa o valor associado à chave 
#"'nome'" em cada dicionário, que é o critério usado para ordenar os elementos da lista.
l1 = sorted(lista, key=lambda item: item['nome'])
print(l1)