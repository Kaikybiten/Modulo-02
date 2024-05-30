def decorador(func):
    print('ola')
    def interna(*args):
        res = func(*args)
        res += 100
        return res
    return interna

@decorador
def soma(x, y): # Linha 10 e 11 é o mesmo que chamar a função decorador com decorador(soma)
    return x + y

print(soma(2,3))