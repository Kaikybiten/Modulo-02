lista = [1,2,3,4,5,6,7,8,9]

mudar = map( 
    lambda x: x * 10, 
    lista
    )

print(next(mudar))
print(next(mudar))
print(next(mudar))
print(next(mudar))

filtro = filter(
    lambda x: (x % 2) == 0,
    lista
)

print(next(filtro))
print(next(filtro))
print(next(filtro))
print(next(filtro))