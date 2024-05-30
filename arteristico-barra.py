# x e y se tornaram argumentos posicionais, ou seja, quando a função for chamada deve seguir o posicionamento dos argumentos.
def barra(x, y, /):
    print(x + y)

# Todos os argumentos a esquerda do asteristico serão sugados para o argumento args, a não ser que o argumento a esquerda seja declarado, ex: y=4
def asterisco(x, *args, y):
    x = 0
    x *= args
    print(x + y)