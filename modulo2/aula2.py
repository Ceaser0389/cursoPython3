"""
Argumentos nomeados e não nomeados em funções Python
argumento nomeado tem o nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor
se vc nomeaum valor o o porximo deve ser nomeado
     ex soma(1,y=2,z=5)
"""

def sub(x,y):
    print(x-y)

sub(5,3)


def soma(x,y):
    #definição
   print(f'{x=} y{y}', '|', 'x = y = ', x + y)

soma(y = 2,x = 1) # argumento nomeado
    
