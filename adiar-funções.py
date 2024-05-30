def criarMultiplicador(x):
    def multiplicar(y):
        return x * y
    return multiplicar

duplicar = criarMultiplicador(2)
triplicar = criarMultiplicador(3)
quadruplicar = criarMultiplicador(4)

print(duplicar(5))
print()
print(triplicar(5))
print()
print(quadruplicar(5))

def inicial(primeiraString):
    inicio = primeiraString
    
    def concatenar(proxima):
        return inicio + ' ' + proxima
    return concatenar

oi = inicial('opa, meu amigo')

print(oi('caio'))
print()

def letra(x):
    primeira = x
    
    def letras(x):
        nonlocal primeira
        primeira += x
        return primeira
    
    return letras

alfabeto = letra('a')

alfabeto('bcd')
alfabeto('efghijk')

print(alfabeto('fim'))