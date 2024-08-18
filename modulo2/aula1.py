"""
Introdução ás funções (def) em Python
Funções são trechos de código usados para replicar
determrminada  ação ao  longo de seu código.
Elas podem receber valores para parâmetros(argumentos)
e retornar um valor específico.
por, padrão funções Python retornam None(nada)
 valor em si é argumentos, parametros as variaveis passadas no metodo
"""
def imprimir():
    print('Olá César bem vindo  a linguagem Python')

def imprimir2(a,b,c):
        print(a,b,c)

def saudacao(nome):
        print(f'Olá,{nome}!')


imprimir()
print('*******************************')

imprimir2(1,2,3)

print('*******************************')
saudacao('César Alves')
