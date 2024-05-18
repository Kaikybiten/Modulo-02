# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

string = [ i for i in lista if isinstance(i, str)]

print(string)

numero = [i for i in lista if isinstance(i, (int, float))]

print(numero)

