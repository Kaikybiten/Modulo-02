# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criarMultiplicador(multiplo): # Daqui cria a função e pula pra linha 8
    def multiplicar(numero):
        return numero * multiplo
    return multiplicar # Quando a função "criarMultiplicador" for executada ela retornará a função multiplicar com o valor de "multiplo" dentro dela

duplicar = criarMultiplicador(2) # Pula para dentro da função criarMultiplicador e define "multiplo" como 2
triplicar = criarMultiplicador(3) # Pula para dentro da função criarMultiplicador e define "multiplo" como 3
quadruplicar = criarMultiplicador(4) # Pula para dentro da função criarMultiplicador e define "multiplo" como 4

print(duplicar(4)) # Executa a função multiplicar e define "numero" como 4
print(triplicar(4)) # Executa a função multiplicar e define "numero" como 4
print(quadruplicar(4)) # Executa a função multiplicar e define "numero" como 4