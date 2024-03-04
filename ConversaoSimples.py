escolha=float(input("1 - Fahrenheit \n2 - Kelvin \n3 - Rankine \n4 - Réaumur \nEscolha qual conversão fazer: "))
if(escolha == 1):
    fah=float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (5 * (fah - 32)) / 9
    print("Valor em celsius: ", celsius)
elif(escolha == 2):
    kel=float(input("Digite a temperatura em Kelvin: "))
    celsius = (kel - 273,15)
    print("Valor em celsius: ", celsius)
elif(escolha == 3):
    ran=float(input("Digite a temperatura em Rankine: "))
    celsius = ((5 * ran)/9) - 273.15
    print("Valor em celsius: ", celsius)
elif(escolha == 4):
    rea=float(input("Digite a temperatura em Réaumur: "))
    celsius = (5 * rea) / 4
    print("Valor em celsius: ", celsius)
else:
    print("Escolha invalida.")