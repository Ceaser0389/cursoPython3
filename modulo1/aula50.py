
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - indíces e fatiamento
Métodos úteis: append, insert, pop , del, clear, extend, + Create, read,update delete

lista é bom tirar coisas só no final
"""

lista = [10,20,30,40]
print(lista[2])                 # ler um valor
print("*****************")


numero = lista[2] = 300        # alterar um valor
print(lista)
print("*****************")

del lista[2]                 # apagar um valor da lista
print(lista)
print(lista[2])
print("*****************")


lista.append(50)           # add no fim da lista
print(lista)
print("*****************")

lista.pop()               # remove ultimo elemento da lista
print(lista)
print("*****************")

lista.insert(0,5)         # isere em um determinado valor na lista  insert(indice,valor)
print(lista)
print("*****************")

