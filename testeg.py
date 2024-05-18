import sys

gen = (i for i in range(1000))

for j in gen:
    print(j)

print(sys.getsizeof(gen))

