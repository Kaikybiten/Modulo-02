from functools import reduce

lista = [23, 45, 67, 10]

total = reduce(
    lambda acumulador, item: acumulador + item,
    lista,
    0
)

print(total)

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

soma = reduce(
    lambda acumulador, item: acumulador + item['preco'],
    produtos,
    0
)

print(soma)



res = 0

for x in produtos:
    res += x['preco']

print(res)
    