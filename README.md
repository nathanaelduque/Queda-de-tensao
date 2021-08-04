# Queda-de-tensao
Programa que irá calcular a queda de tensão em um determinado trecho do ramal, ao se colocar uma nova carga sobre o mesmo. Para fazer tal cálculo ele pedirá alguns dados de entrada, tais como:

- Código Canadense do Cabo Utilizado 
- Potência Máxima que a Carga irá ter 
- Fator de Potência da Rede
- Comprimento do Cabo 
- A tensão nominal do sistema 

A partir desses dados,calcula-se o Kdroop do cabo escolhido,para tal processo, usa-se a aproximação:
<p align="center">Vdroop = Re{Z.I}</p>

Onde:

- Z: Impedância do cabo

- I:corrente da carga a ser alocada

E por fim,tem-se que:
p align="center">ΔV= Kdroop.potência.comprimento</p>


*OBS: Para Tal calculo foram usadas as distâncias padrão entre AB,BC E AC, sendo as mesmas 762 [m],1,3716 [m] e Dac= 2,1336 [m], respectivamente.*
