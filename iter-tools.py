def pi(iter):
    lista = (iter)
    print(*lista, sep='\n')
    print()


from itertools import combinations, permutations, product

pessoas = ['joão', 'paula', 'gabi', 'pedro']

pi(combinations(pessoas, 2)) # Todas as combinações, sem nenhuma repetição

pi(permutations(pessoas, 2)) # Novamente, todas as combinações, porém dessa vez com repetições

camisas = [
    ['branca', 'preta', 'colorida'],
    ['p', 'm', 'g'],
    ['algodão', 'poliester']
]

pi(product(*camisas))