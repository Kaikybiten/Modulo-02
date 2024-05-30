from functools import partial # Função que guarda uma função + quantos argumentos o usuario/dev quiser

def aumentarPorcentagem(valor, porcentagem):
    return valor + valor * porcentagem/100

aumentarDezPorcento = partial(aumentarPorcentagem, porcentagem=10)
aumentarCinquentaPorcento = partial(aumentarPorcentagem, porcentagem=50)

valorAtual = aumentarDezPorcento(100)
print(valorAtual)

valorAtual = aumentarCinquentaPorcento(100)
print(valorAtual)

