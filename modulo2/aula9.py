"""
args -Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-se de desempacotamento
x, y, *resto = 1, 2 , 3, 4,
print(x,y,resto)

def soma(x,y):
    return x + y

def soma(*args):              # argumentos n nomeados
    total = 0
    for numero in args:
        total += numero
    return  total


soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

soma_4_5_6 = soma(4,5,6)
print(soma_4_5_6)

outra_soma = soma(1,2,3,4,5,6,7)
print(outra_soma)

