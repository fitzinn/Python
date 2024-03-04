import math as m

#leitura
ang=float(input("Digite o Angulo: "))
vi=float(input("Digite a Velocidade Inicial: "))
t=float(input("Digite o Valor do Tempo: "))
g=10

#calculos
ang_rad = m.radians(ang)
x=vi*(m.cos(ang_rad))*t
y=vi*(m.sin(ang_rad))*t-((10*(t*t))/2)

#imprimir
print("Valor da Distancia: ", format(x, "5.2f"))
print("Valor da Altura: ", format(y, "5.2f"))