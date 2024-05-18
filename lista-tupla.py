import sys

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Tuplas ocupam menos espaço na memoria, comparado a Listas
print(type(lista), sys.getsizeof(lista))
print(type(tupla), sys.getsizeof(tupla))