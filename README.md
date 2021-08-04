# Queda-de-tensao
Programa que irá calcular a queda de tensão em um determinado trecho do ramal, ao se colocar uma nova carga sobre o mesmo. Para fazer tal cálculo ele pedirá alguns dados de entrada, tais como:

- Código Canadense do Cabo Utilizado 
- Potência Máxima que a Carga irá ter(S) 
- Fator de Potência da Rede(fp)
- Comprimento do Cabo (L)
- A tensão nominal do sistema(V) 

A partir desses dados,calcula-se o Kdroop do cabo escolhido,para tal processo, usa-se a aproximação:
<p align="center">Vdroop = Re{Z.I}</p>

Onde:

- Z: Impedância do cabo

- I:corrente da carga a ser alocada

E por fim,tem-se que:
<p align="center">ΔV= Kdroop.S.L</p>


*OBS: Para Tal calculo foram usadas as distâncias padrão entre AB,BC E AC, sendo as mesmas 762 [m],1,3716 [m] e Dac= 2,1336 [m], respectivamente.Tais distâncias podem ser vistas na Figura 01.*




<p align="center">Figura 01:Distância entre os cabos</p>

<p align="center">

  <img width="400" src="https://github.com/nathanaelduque/Queda-de-tensao/blob/main/Separa.png" alt="Material Bread logo">
  
</p>
