import math as m

#leitura
pox=float(input("Digite a coordenada X da origem: "))
poy=float(input("Digite a coordenada y da origem: "))
pdx=float(input("Digite a coordenada X do destino: "))
pdy=float(input("Digite a coordenada y do destino: "))

#calculos
d=m.sqrt((pdx - pox)**2 + (pdy - poy)**2)

#imprimir
print("Distancia Linear entre os pontos: ", format(d, "10.2f"))