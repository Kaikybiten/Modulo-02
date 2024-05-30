import itertools

contador = itertools.count()

for i in range(100):
    print(next(contador))