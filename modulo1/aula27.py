
nome = input('Digite o seu nome:')
idade = input('Digite a sua idade:')

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    if '' in nome:
        print('Seu nome N contém espaços')
    else:
        print('Seu nome NÂO contém espaços')

    print(f'seu nome tem {len(nome)} letras')
    print(f'seu nome é {nome[0]}')
    print(f'seu nome é {nome[-1]}')
else:
    print("Desculpe,você deixou campos vazios")