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

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

print(p1.get('nome', 'Nome não Existe'))

nome = p1.pop('nome')
print(nome)
print(p1)
print('------------------------------')

ultima_chave= p1.popitem()
print(ultima_chave)

print(p1)

print('------------------------------')

p1.update({
    'nome': 'Novo Valar',
    'idade': 30,
})
print(p1)
print('------------------------------')

p1.update(nome='novo valor', idade=30)
print(p1)
print('------------------------------')


tupla = (('nome','novo valor'),('idade', 30))
p1.update(tupla)
print(p1)
print('------------------------------')

lista = [['nome', 'novo valor'], ['idade ', 30]]
p1.update(lista)
print(p1)