# Exercício - Adiando execução de funções

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x): 
    def criada(y): # Cria função que pede o (y) que no caso é o unico argumento que falta
        return funcao(x, y)
    return criada # Devolve a função que espera o (y) porem na memoria dela já esta guardada o valor de x    

soma_com_cinco = criar_funcao(soma, 5) # Salva função da linha 9

print(soma_com_cinco(7))

multiplica_por_dez = criar_funcao(multiplica, 10)