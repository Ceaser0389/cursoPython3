# exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)

    if 'l' in letras:
        print('Parabéns')
        breakpoint

    print(letras)