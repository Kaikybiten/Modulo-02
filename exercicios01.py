# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    result = 1
    for number in args:
        result *= number
    return result

result = mult(1,2,3,4,5,6,7,8,9)

print(result)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def oddEven(number):
    if (number % 2 == 0):
        return 'Par'
    return 'Impar'

print(oddEven(4))