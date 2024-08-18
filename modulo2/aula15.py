"""
 Métodos úties dos diciónarios em Python
 len - quantas chaves
 Keys - interável com as cheves
 values - iterável com os valores
 items - iterável com chaves e valores
 setdefault = adiciona valor se a chave não existe
 copy - retorna uma cópia rasa (shally copy)
 get - obtém uma chave
 pop =- Apaga um item com a chave especifica (del)
 popItem - apaga o último item adicionado
 update - Atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda 1',
    #'idade':900
}

print(len(pessoa))  # qtd chaves no dict
print('-----------------------------------')

print(list(pessoa.keys()))
print('-----------------------------------')

print(list(pessoa.values()))                # verifica os valores
print('-----------------------------------')

print(list(pessoa.items()))                # mostra a chave e o valor
print('-----------------------------------')

for valor in pessoa.values():
   print(valor)

print('-----------------------------------')

for chave, valor in pessoa.items():
   print(chave,valor)


pessoa.setdefault('idade',0)
print(pessoa['idade'])

