    # Criando uma lista de forma dinamica
#nome   #adicionar      #vezes
lista = [1 for numero in range(10)]
print(lista) #Retorna [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], retorna "1" 10 vezes

lista = [numero for numero in range(10)]
print(lista) #Retorna [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], retorna os numeros iterados do range(10)

lista = [numero * 2 for numero in range(10)]
print(lista) #Retorna [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], retorna todas os numeros do range(10), porem todos multiplicados por 2

lista = [numero * numero for numero in range(10)]
print(lista) #Retorna [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], basta seguir a logica...

#list comprehension composta
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)

lista = [
    j
    for i in lista
    for j in i
]
print(lista)


    # Com dicionarios
produtos = [
    {'nome' : 'p1', 'preco' : 30},
    {'nome' : 'p2', 'preco' : 38},
    {'nome' : 'p3', 'preco' : 65},
    {'nome' : 'p4', 'preco' : 15},
]

novosPrecos = [
    {**produto, 'preço' : produto['preco'] * 10 / 100} for produto in produtos
     ]

print(novosPrecos)
