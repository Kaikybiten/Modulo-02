produtos = [
    {'produto' : 'cama', 'preco' : 300},
    {'produto' : 'mesa', 'preco' : 250},
    {'produto' : 'celular', 'preco' : 1000},
    {'produto' : 'espelho', 'preco' : 150}
]

# Dê 50% de desconto em todos os produtos
produtosDesconto = [
    # Inicia adicionando os primeiros itens, e após adiciona a segunda chave porém cortando 50% dela
    {**produto, 'preco': produto['preco'] * 50 / 100} for produto in produtos
]
print(produtosDesconto)

# Exclua todos os produtos de 1000 para cima
produtosBaratos = [
    produto for produto in produtos if produto['preco'] < 1000
]
print(produtosBaratos)

# Aumente o valor em 5% de todos os produtos que custem menos de 300
aumentoValores = [
    {**produto, 'preco': produto['preco'] * 105 / 100} if produto['preco'] < 300 else {**produto} for produto in produtos
]
print(aumentoValores)
