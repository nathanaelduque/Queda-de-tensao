import pandas as pd
import numpy as np
import math

'''

Esse programa irá pedir o condutor usado, o comprimento do mesmo,o fator de potência e a potência 
que irá fluir no condutor,e a partir disso, ele irá calcular a queda de tensão no trecho através 
do método do Cálculo do Kdroop.

'''

#Importando os dados necessários da planilha de caracteristicas de cada condutor
caracteristicas=pd.read_excel('Cabos.xlsx')

#Coletando os dados que serão uteis:
util=list()
util.append(caracteristicas['Código'])
util.append(caracteristicas['Diâmetro Externo Nominal (mm)'])
util.append(caracteristicas['Resistência(Ohm/km)'])

#Transformando num array
util=np.array(util)

print("-------------------------------------")
print(" Qual o código do condutor utilizado? ")
print(" Exemplos de resposta:")
print(" Rose,Aster,Valerian")
cd=input(" R:")
print("-------------------------------------")


if cd in util[0]:
    arg=np.where(util[0]==cd) #usaremos os argumentos para pegarmos os valores de resistência e de GMR
    arg=arg[0][0] # para a função retornada ser um inteiro
    print("Agora dê o comprimento do mesmo em quilometros")
    comp=float(input(" R:"))
    print("-------------------------------------")
    print("Dê agora o fator de potência da rede")
    fp=float(input(" R:"))
    print("-------------------------------------")
    if abs(fp)<=1:
        print("Dê também a potência que vai fluir pelo mesmo em VA")
        pot=float(input(" R:"))
        print("-------------------------------------")
        print("Por fim,dê a tensão de linha do sistema, em volts")
        V=float(input(" R:"))
        print("-------------------------------------")
    else:
        raise Exception("Você forneceu um fator de potência maior que 1!")
    
else:
    raise Exception("Desculpe,mas esse código não está na tabela!")

Dab=0.762
Dbc=1.3716
Dac=Dab + Dbc

#Calculando a Deq para usar na fórmula da sequência positiva
Deq=(Dab*Dbc*Dac)**(1/3)

#formula da sequência positiva (util[1][arg]/2 --> A tabela nos dá o diametro, precisamos do raio)
zpositiva =complex(util[2][arg],0.12134*math.log(Deq/((10**-3)*util[1][arg]/2)))

# Calculando a corrente do Kdroop
I=complex(fp*1000/(V*math.sqrt(3)),-1*math.sqrt(1-(fp**2))*1000/(V*math.sqrt(3)))

#Aproximando o Vdroop da parte real do mesmo
Vdroop = (zpositiva*I).real

#Calculando o Kdroop  (V/math.sqrt(3)--> Tensão de fase do sistema)
Kdroop=100*(Vdroop/(V/math.sqrt(3)))

print("\n ################# Resultados #################")
print("O Kdroop do mesmo será:",Kdroop)

#Calcula-se, por fim , a queda de tensão
qtensao=Kdroop*pot*comp

print("E a queda de tensão será:",qtensao,"[%]")
print("-------------------------------------")

print("Para fazer esses calculos, foram utilizadas as distâncias padrão de espaçamento entre os condutores:")
print("Dab =0,762 [m],Dbc=1,3716 [m] e Dac= 2,1336 [m]")

print("----------------OBS---------------------")
