"""
Higher Order Functions          função  pode ser tratada como qualquer tipo d dado
Funções de primeira classe
"""

def saudacao(msg,nome):
    return f'{msg}, {nome}'

def executa(funcao,*args):
    return funcao(*args)



print(
    executa(saudacao,'Bom dia', 'César')
)

print(
    executa(saudacao,'Bom dia', 'Gael')
)