"""
CONSTANTE = "Variáveis" que não vão mudar
muitas condições no memso if(ruim)
<- Contagem de complexidade(ruim)

no python tem convenção p constante tudo em MAIUSCULO -> RADAR_1
"""

velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE =1

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)

local_carro <= (LOCAL_1 + RADAR_RANGE)


if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if  carro_multado_radar_1 and vel_carro_pass_radar_1:
    print('Carro multado em radar 1')



