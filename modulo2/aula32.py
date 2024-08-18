# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

print(produto.items())



dc = {
    chave: valor.upper()
    if isinstance(valor,str) else valor
    for chave, valor
    in produto.items()
    if chave == 'categoria'
}

print(dc)