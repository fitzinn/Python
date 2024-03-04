vd1=float(input("Valor Distancia Trecho 1: "))
vt1=float(input("Valor Tempo Parte 1: "))

vd2=float(input("\nValor Distancia Trecho 2: "))
vt2=float(input("Valor Tempo Parte 2: "))

vd3=float(input("\nValor Distancia Trecho 3: "))
vt3=float(input("Valor Tempo Parte 3: "))

vd4=float(input("\nValor Distancia Trecho 4: "))
vt4=float(input("Valor Tempo Parte 4: "))

#calculo cada trecho
vm1=vd1/vt1
vm2=vd2/vt2
vm3=vd3/vt3
vm4=vd4/vt4

#calculo distancia total
dt=vd1+vd2+vd3+vd4

#calculo tempo total
tt=vt1+vt2+vt3+vt4

#calculo velocidade media
vm=dt/tt

#calculo aceleracao
ac1=(vd1-vd2)/vt1+vt2
ac2=(vd2-vd3)/vt2+vt3
ac3=(vd3-vd4)/vt3+vt4

#imprimir velocidade media trecho
print("\nVelocidade Media Trecho 1: ", format(vm1, "7.2f"))
print("Velocidade Media Trecho 2: ", format(vm2, "7.2f"))
print("Velocidade Media Trecho 3: ", format(vm3, "7.2f"))
print("Velocidade Media Trecho 4: ", format(vm4, "7.2f"))

#imprimir velocidade media total
print("\nVelocidade Media Total: ", format(vm, "7.2f"))

#imprimir aceleracao
print("\nAceleração entre Trecho 1 e Trecho 2: ", format(ac1, "7.2f"))
print("Aceleração entre Trecho 2 e Trecho 3: ", format(ac2, "7.2f"))
print("Aceleração entre Trecho 3 e Trecho 4: ", format(ac3, "7.2f"))