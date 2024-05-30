#expondo erros
def int_float(operando):
    if not isinstance(operando, (int, float)):
        raise TypeError(
            f'{operando} is not a number. '
            f'{operando} is a {type(operando).__name__}'
        )
    return True

def notzero(operando):
    if operando == 0:
        raise ZeroDivisionError('Não é possivel dividir por zero')
    return True

def divide(a, b):
    int_float(a)
    int_float(b)

    notzero(a)
    notzero(b)

    return a / b

print(divide(10,2))