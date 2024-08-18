# Exercícios com funções

# crie uma função que mult todos os argu
# não nomeados recebidos
# Retorne o total para uma variavel para uma variável e mostra o valor da mesma

def multiplicar(*args):
    total= 1
    for numero in args:
       total *= numero
    return  total

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)


# Crie um função fala se um n é par ou ímpar
# Retorne se o número é par ímpar


def par_impar(numero):
    multiplo_de_dois =  numero % 2  == 0

    if multiplo_de_dois:
        return  f'{numero} é par'
    return f'{numero} é impar'
    

print(par_impar(2))
print(par_impar(3))
print(par_impar(4))