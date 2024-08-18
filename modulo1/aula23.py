# Operadores in e not in
# Strings são interáveis

nome = 'César'
# print(nome[2])
# print(nome[-4])

print('C' in nome)
print('Z' in nome)

nome = input('Digite o seu nome:')
encontrar = input('Digite oque deseja encontrar:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')