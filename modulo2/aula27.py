# Empacotamento e desencotamento de dicionários

a, b = 1,2
a,b = b,a
print(a,b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura':1.6,
}

pessoas_completa = {** pessoa, **dados_pessoa}
print(pessoas_completa)



# args e kwars
# args (já vimos)
# kwars - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwards):
    print('Não Nomeados', args)

    for chave, valor in kwards.items():
        print(chave,valor)


mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'args1': 1,
    'args2': 2,
    'args3': 3,
    'args4': 4,
}
mostro_argumentos_nomeados(**configuracoes)    
