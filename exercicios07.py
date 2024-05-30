# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']
uniao   = []

iCidades = iter(cidades)
iEstados = iter(estados)

for i in cidades:
    uniao.append((next(iCidades), next(iEstados)))

print(uniao)

# Ou simplesmente

combinado = zip(cidades, estados)
combinado = list(combinado)
print(combinado)

# Versão baseada na maior lista

import itertools

listaCombinada = itertools.zip_longest(cidades, estados, fillvalue='Cidade não listada')
listaCombinada = list(listaCombinada)
print(listaCombinada)