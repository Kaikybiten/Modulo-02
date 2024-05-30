import sys

import modularizacao01

print('este é o modulo ', __name__) # Retorna __main__ caso essa seja o primeiro modulo executado, caso contrario, irá retornar o nome do modulo

# Lugares que o python busca modulos
caminhos = iter(sys.path)

for i in range(len(sys.path)):
    print(next(caminhos))