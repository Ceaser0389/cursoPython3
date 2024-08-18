"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - indíces e fatiamento
Métodos úteis: append, insert, pop , del, clear, extend, + Create, read,update delete
"""

string = 'ABCD' # 5 caracteres(len)

#         0   1     2              3 4
#         -5  -4    -3            -2 -1
lista = [123,True,'Cesar Alves ',1.2,[]]
print(lista)
print("************************************")

print(lista[2],type(lista[2]))
#print(lista,type(lista))

print("************************************")
lista[-3] = 'Maria'
print(lista)