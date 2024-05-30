"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
lista_soma  = []

def somandoListas(l1,l2):
    combinado = zip(l1,l2)
    for i,j in combinado:
        soma = i + j
        lista_soma.append(soma)
    return lista_soma
    
print(somandoListas(lista_a, lista_b))

# Ou

def somarListas(l1,l2):
    listaSomada = [x + y for x, y in zip(l1,l2)]
    return listaSomada

print(somarListas(lista_a, lista_b))

# Versão baseada na maior lista
import itertools

def somaLista(l1, l2):
    listaSoma = [x + y for x, y in itertools.zip_longest(l1, l2, fillvalue=0)]
    return listaSoma

print(somaLista(lista_a, lista_b))