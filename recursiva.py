def recursiva(inicio=0, fim=10):
    if inicio >= fim:
        print (f'valor final: {inicio}') # comando teste
        return inicio
    
    inicio += 1
    print(f'valor atual: {inicio}') # comando teste
    return recursiva(inicio, fim)

recursiva()

def fatorial(n=5):
    def fato(n):
        if n <= 1:
            return 1
        else:
            return n * fato(n - 1)
    return fato(n)