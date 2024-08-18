"""
Imprecisão do ponto flutuante
double-precision floting-point Format IEEE 754
"""
# tem o modulo do python  import decimal(usa para numeros float muitos grandes)
# modulo decimal uma opção p calculo preciso (numero flutuante muito grande)


numero_1 = 0.1
numero_2 = 0.2
numero_3 =  numero_1 + numero_2

print(numero_3)

# tipo um para formatar
print(f'{numero_3:.2f}')

# função para formatar
print(round(numero_3,3))



