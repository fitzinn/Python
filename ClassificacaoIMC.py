altura=float(input("Digite sua altura: "))
peso=float(input("Digite o seu peso: "))

imc = peso / (altura * altura)
if(imc>=30):
    #obeso
    print("Classificação: Obeso")
elif(imc>=25):
    #sobrepeso
    print("Classificação: Sobrepeso")
elif(imc>=18.5):
    #normal
    print("Classificação: Normal")
elif(imc<18.5):
    #baixopeso
    print("Classificação: Baixo peso")