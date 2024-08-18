# List comprehension em Python
# List comprehension é uma fomra rápida para criar listas
# a partir de interáveis
#print(list(range(10)))

lista = []


for numero in range(10):
    lista.append(numero)

#print(lista)

lista = [
        numero * 2
        for numero in range(10)
        ]
print(lista)

# mapeamento de dados em  lis comprehension

produtos = [
     {'nome': 'p1', 'preco':20},
     {'nome': 'p1', 'preco':10},
     {'nome': 'p1', 'preco':30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05 }
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

#print(*novos_produtos, sep='\n')

lista = [ n for n in range(10) if n < 5]
print(lista) 