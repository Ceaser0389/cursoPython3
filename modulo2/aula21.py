# Sets - Conjuntos em python (tipo set)
# Conjuntos são ensinados na matemática
# Sets em python são mutáveis. porém aceitam apenas 
# tipos  imutáveis como valor interno

# Criando um set
# Set (interável) ou {1,2,3}
#s1 = set() #vazio
#s1 = {'luiz',1,2,3} # com dados


# Sets são eficientes para remover valores duplicados de iteráveis.
# eles não tem índexes
# eles não garatem ordem
# eles são interáveis ( for, in , not in)
#s1 = {1,2,3,3,3,3,3,}

#s2 = s2 ={1,2,3,[123]}   ex interáveis



# Métodos úteis
# add, update , clear, discard

s1 = set()
s1.add('luiz')
s1.update(('Olá mundo',1,2,3,4,5)) #passar varios valores
print(s1)
print('-------------------')
#s1.clear() #limpa
s1.discard('Olá mundo')
print(s1)
