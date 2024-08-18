
"""
enumerate - enumera interáveis(índices)
"""

lista = ['Maria','helena','Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

#for item in lista_enumerada:
 #   print(item)

for indice, nome in enumerate(lista):
    print(indice,nome)
