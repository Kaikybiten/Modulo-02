def soma(*args):
    total = 0
    for number in args:
        total += number
    return total

resultado00 = soma(58, 73, 56, 99, 102)
print(resultado00)

numeros = 58, 73, 56, 99, 102
resultado01 = soma(*numeros) # * desempacota os valores dentro da tupla

print(*numeros)