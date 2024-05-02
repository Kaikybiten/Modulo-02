# Criando um set
s1 = set() #ou {valores}
print(s1)

# Adicionando iteraveis
s1 = set('Luiz')
print(s1) # Nesse caso as letras irão ser impressas de forma embaralhada, cada uma sendo um valor diferente

s1 = {'luiz'} 
print(s1) # Já nesse, as letras estarão em ordem, porquê todas estão juntas, formando apenas um valor

# Sets eliminam valores iguais, deixando apenas um
s1 = {1,2,3,3,4,4,4,4,5,5,5}
print(s1)

# Adicionado um valor
s1.add(7)
print(s1)

# Adicionando um iteravel ao set
s1.update(('luiz',87,65,43))
print(s1)

# Deletando um valor do set
s1.discard('luiz')
print(s1)

    # Tratando os conjuntos
c1 = {12, 23, 34, 45, 56}
c2 = {12, 23, 43, 54, 65}

# Unindo os conjuntos
uniao = c1 | c2
print(uniao)

# Descobrindo os valores que estão em ambos
interseccao = c1 & c2
print(interseccao)

# Descobrindo quais valores estão presentes apenas no conjunto da esquerda
diferenca = c1 - c2
print(diferenca)

# Descobrindo quais itens não estão presentes em ambos
diferencaSimetrica = c1 ^ c2
print(diferencaSimetrica)