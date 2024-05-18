def entrada_carro():
    carros = []

    for _ in range(4):
        carros.append(input())
        
    return carros
    
def entrada_consumo():
    consumos = []

    for _ in range(4):
        consumo = int(input())
        consumos.append(consumo)

    return consumos

def economico(consumos, carros):
    organizada = sorted(consumos)
    indice = consumos.index(organizada[0])
    return carros[indice]

def main():
    carros = entrada_carro()
    consumos = entrada_consumo()
    print(economico(consumos, carros))

main()