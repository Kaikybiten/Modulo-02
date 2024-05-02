def parImpar(imparPar, ate):
    if imparPar == 'par':
        pares = [p for p in range(ate + 1) if p % 2 == 0]
        return pares
    if imparPar == 'impar':
        impares = [i for i in range(ate + 1) if i % 2 != 0]
        return impares

print(parImpar('impar', 50))