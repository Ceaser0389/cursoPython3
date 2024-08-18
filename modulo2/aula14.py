#dicionários são estruturas de dados tipo valor
#Usadmos as chaves - {} - ou a calsse dict para criar dicnários
#pode ser usado qualquer valor  Imutáveis, str, int , flot, bool , tuple
#mutável dict, list

#pessoa =dict(nome="Luiz", sobrenome="Miranda")

pessoa ={
    'nome':'Luiz Otávio',
    'Sobrenome': 'Miranda',
    'idade':18,
    'altura':1.8,
    'endereços': [
        {'rua': 'tal tal', 'número':123},
        {'rua': 'outra rua', 'numero':321}
    ]
}
print(pessoa,type(pessoa))
print(pessoa['nome'])
print(pessoa['Sobrenome'])


for chave in pessoa:
    print(chave,pessoa[chave])



    