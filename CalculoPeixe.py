mp1=float(input("Digite a Massa do Peixe 1: "))
cp1=float(input("Digite o Comprimento do Peixe 1: "))

mp2=float(input("\nDigite a Massa do Peixe 2: "))
cp2=float(input("Digite o Comprimento do Peixe 2: "))

mp3=float(input("\nDigite a Massa do Peixe 3: "))
cp3=float(input("Digite o Comprimento do Peixe 3: "))

mp4=float(input("\nDigite a Massa do Peixe 4: "))
cp4=float(input("Digite o Comprimento do Peixe 4: "))

mp5=float(input("\nDigite a Massa do Peixe 5: "))
cp5=float(input("Digite o Comprimento do Peixe 5: "))

mp6=float(input("\nDigite a Massa do Peixe 6: "))
cp6=float(input("Digite o Comprimento do Peixe 6: "))

mp7=float(input("\nDigite a Massa do Peixe 7: "))
cp7=float(input("Digite o Comprimento do Peixe 7: "))

#calculo
sc = cp1 + cp2 + cp3 + cp4 + cp5 + cp6 + cp7
m = (mp1 * cp1 + mp2 * cp2 + mp3 * cp3 + mp4 * cp4 + mp5 * cp5 + mp6 * cp6 + mp7 * cp7) / sc

#imprimir
print("Media Ponderada da massa dos peixes: ", format(m, "10.2f"))