listaComum      =   [i for i in range(100)]
print(listaComum) # Irá imprimir todos os numeros de 0 à 99

listaGenerator  =   (i for i in range(100))
print(listaGenerator) # Irá imprimir um espaço da memoria

# A listaComum está ocupado muito mais espaço da memoria do que a listaGenerator, porquê enquanto uma guarda todos os numeros de 0 a 99, a outra só guarda o numero que será exibido 

import sys

def quantidadeDeBits(lista):
    print(sys.getsizeof(lista))

# Revelando quantos bits cada uma das lista tem e ocupa na memoria

quantidadeDeBits(listaComum)        # 115 bytes = 920 bits
quantidadeDeBits(listaGenerator)    # 24 bytes  = 192 bits

# Generator funciona como um iterador, que não possui noção da sua magnitude, apenas do proximo numero que ele guarda
print(next(listaGenerator)) # 0
print(next(listaGenerator)) # 1
print(next(listaGenerator)) # 2
print(next(listaGenerator)) # 3
print(next(listaGenerator)) # 4
print(next(listaGenerator)) # 5
print(next(listaGenerator)) # 6
print(next(listaGenerator)) # 7
print(next(listaGenerator)) # 8
print(next(listaGenerator)) # 9
print(next(listaGenerator)) # 10
print('fim')
print()
# A cada chamada da função "next" o valor anterior é perdido


#       Generator com em funções
def generator():
    yield 1 # Pausa a função aqui e retorna 1
    yield 2 # Pausa a função aqui e retorna 2
    yield 3 # Pausa a função aqui e retorna 3
    yield 4 # Pausa a função aqui e retorna 4
    yield 5 # Pausa a função aqui e retorna 5

    return 'acabou' # Neste caso o return se torna uma exception, para o erro StopIteration

# Enquanto o retun encerra a função, o yield apenas faz uma pausa

gen = generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# yield from (dar continuidade em um generator apartir de outro)
def gen1():
    yield from gen2()
    yield 11
    yield 12
    yield 13

def gen2():
    yield 21
    yield from gen3()
    yield 22
    yield 23

def gen3():
    yield 31
    yield 32
    yield from gen1()
    yield 33

g = gen1()

for i in g:
    print(i)
    input()