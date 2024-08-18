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

import copy


d1 = {                        # valor mutavel  copy não funciona
    'c1':1,
    'c2':2,
    'l1': [0,1,2]
}

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 999999


print(d1)
print(d2)

