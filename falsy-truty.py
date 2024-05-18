#    Todas essas listas retornam o valor "False"
# Ausencia de valor = False

dicionario  =   {}
intervalo   =   range(0)
flutuante   =   0.0
conjunto    =   set()
boleano     =   False
inteiro     =   0
string      =   ''
lista       =   []
tupla       =   ()
nada        =   None

# Função para revelar o retorno boleano
def falsy(tipo):
    return 'truthy' if tipo else 'falsy'