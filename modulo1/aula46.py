"""
 for + Range
 range -> range (start,stop,step)
 next ->  entrega o proximo valor
 iter -> me entregue seu iterador( entrega obj interador)

 
"""

numeros = range(0,100,7)

for numero in numeros:
    print(numero)

print('************************')

texto = iter('Cesar')

print(texto.__next__())
