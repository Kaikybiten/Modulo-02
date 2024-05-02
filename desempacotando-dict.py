identidade = {
    'nome' : 'kaiky',
    'sobrenome' : 'bitencourt'
}

a, b = identidade
print(a, b) # Retorna as chaves "nome sobrenome"

a, b = identidade.values()
print(a, b) # Retorna os valores "kaiky bitencourt"

a, b = identidade.items()
print(a, b) # Retorna as chaves e os valores "('nome', 'kaiky') ('sobrenome', 'bitencourt')" em tuplas


    # DESEMPACOTAMENTO INTERNO

(a1, a2), b = identidade.items()
print(a1, a2) #Retorna a primeira chave e valor "nome kaiky" fora de tuplas

a, (b1, b2) = identidade.items()
print(b1, b2) #Retorna a segunda chave e valor "sobrenome bitencourt" fora de tuplas

(a1, a2), (b1, b2) = identidade.items()
print(a1, a2, b1, b2) #Retorna todos os valores "nome kaiky sobrenome bitencourt" fora de tuplas

    #Juntando dicionarios em outro dicionario

dados = {
    'idade' : 20,
    'altura' : 1.75
}

pessoaCompleta = {**identidade, **dados}

print(pessoaCompleta)