# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos10 = [
    {**i, 'preco' : round(i['preco'] + i['preco'] * 10 / 100, 2)} for i in produtos
    ]

novos_produtos = copy.deepcopy(produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
produtos.sort(key=lambda produtos: produtos['preco'], reverse=True)
print(*produtos, sep='\n')
print()

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_por_nome = copy.deepcopy(sorted(produtos, key=lambda produtos: produtos['nome']))
print(*produtos_por_nome, sep='\n')
print()

# Ordene os produtos por preco crescente (do menor para maior)
produtos.sort(key= lambda produtos: produtos['preco'])
print(*produtos, sep='\n')
print()

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_por_preco = copy.deepcopy(sorted(produtos, key=lambda produtos: produtos['preco']))
print(*produtos_por_preco, sep='\n')