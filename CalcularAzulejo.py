ls=float(input("Digite a largura da sala: "))
cs=float(input("Digite o comprimento da sala: "))

la=float(input("Digite a largura do azulejo: "))
ca=float(input("Digite o comprimento do azulejo: "))

areas=ls*cs

areaaz=la*ca

npecas=areas/areaaz

print("Numero de peças: ", format(npecas, "5.2f"))