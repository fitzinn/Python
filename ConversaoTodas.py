escolha1=float(input("1 - Fahrenheit \n2 - Kelvin \n3 - Rankine \n4 - Réaumur \n5 - Celsius \nEscolha a escala de origem: "))
escolha2=float(input("1 - Fahrenheit \n2 - Kelvin \n3 - Rankine \n4 - Réaumur \n5 - Celsius \nEscolha a escala de destino: "))

if(escolha1 == 1 and escolha2 == 5):
    #fah para cel
    fah=float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (5 * (fah - 32)) / 9
    print("Valor em celsius: ", celsius)
elif(escolha1 == 2 and escolha2 == 5):
    #kel para cel
    kel=float(input("Digite a temperatura em Kelvin: "))
    celsius = (kel - 273,15)
    print("Valor em celsius: ", celsius)
elif(escolha1 == 3 and escolha2 == 5):
    #ran para cel
    ran=float(input("Digite a temperatura em Rankine: "))
    celsius = ((5 * ran)/9) - 273.15
    print("Valor em celsius: ", celsius)
elif(escolha1 == 4 and escolha2 == 5):
    #rea para cel
    rea=float(input("Digite a temperatura em Réaumur: "))
    celsius = (5 * rea) / 4
    print("Valor em celsius: ", celsius)
elif(escolha1 == 1 and escolha2 == 2):
    #fah para kel
    fah = float(input("Digite a temperatura em Fahrenheit: "))
    kelvin = ((fah - 32) * 5/9) + 273.15
    print("Valor em Kelvin: ", kelvin)
elif(escolha1 == 1 and escolha2 == 3):
    #fah para ran
    fah = float(input("Digite a temperatura em Fahrenheit: "))
    ran = fah + 459.67
    print("Valor em Rankine: ", ran)
elif(escolha1 == 1 and escolha2 == 4):
    #fah para rea
    fah = float(input("Digite a temperatura em Fahrenheit: "))
    rea = ((fah - 32) * 4)/9
    print("Valor em Réaumur: ", rea)
elif(escolha1 == 2 and escolha2 == 1):
    #kel para fah
    kel = float(input("Digite a temperatura em Kelvin: "))
    fah = (((kel - 273.15) * 9)/5) + 32
    print("Valor em Fahrenheit: ", fah)
elif(escolha1 == 2 and escolha2 == 3):
    #kel para ran
    kel = float(input("Digite a temperatura em Kelvin: "))
    ran = (kel * 9)/5
    print("Valor em Rankine: ", ran)
elif(escolha1 == 2 and escolha2 == 4):
    #kel para rea
    kel = float(input("Digite a temperatura em Kelvin: "))
    rea = ((kel - 273.15) * 4)/5
    print("Valor em Réaumur: ", rea)
elif(escolha1 == 3 and escolha2 == 1):
    #ran para fah
    ran = float(input("Digite a temperatura em Rankine: "))
    fah = ran - 459.67
    print("Valor em Fahrenheit: ", fah)
elif(escolha1 == 3 and escolha2 == 2):
    #ran para kel
    ran = float(input("Digite a temperatura em Rankine: "))
    kel = (ran * 5)/9
    print("Valor em Kelvin: ", kel)
elif(escolha1 == 3 and escolha2 == 4):
    #ran para rea
    ran = float(input("Digite a temperatura em Rankine: "))
    rea = ((ran - 491.67) * 4)/9
    print("Valor em Réaumur: ", rea)
elif(escolha1 == 4 and escolha2 == 1):
    #rea para fah
    rea = float(input("Digite a temperatura em Réaumur: "))
    fah = ((rea * 9)/4) + 32
    print("Valor em Fahrenheit: ", fah)
elif(escolha1 == 4 and escolha2 == 2):
    #rea para kel
    rea = float(input("Digite a temperatura em Réaumur: "))
    kel = ((rea * 5)/4) + 273.15
    print("Valor em Kelvin: ", kel)
elif(escolha1 == 4 and escolha2 == 3):
    #rea para ran
    rea = float(input("Digite a temperatura em Réaumur: "))
    ran = ((rea * 9)/4) + 491.67
    print("Valor em Rankine: ", ran)
elif(escolha1 == 5 and escolha2 == 1):
    #cel para fah
    celsius = float(input("Digite a temperatura em Celsius: "))
    fah = ((celsius * 9)/5) + 32
    print("Valor em Fahrenheit: ", fah)
elif(escolha1 == 5 and escolha2 == 2):
    #cel para kel
    celsius = float(input("Digite a temperatura em Celsius: "))
    kel = celsius + 273.15
    print("Valor em Kelvin: ", kel)
elif(escolha1 == 5 and escolha2 == 3):
    #cel para ran
    celsius = float(input("Digite a temperatura em Celsius: "))
    ran = ((celsius * 9)/5) + 491.67
    print("Valor em Rankine: ", ran)
elif(escolha1 == 5 and escolha2 == 4):
    #cel para rea
    celsius = float(input("Digite a temperatura em Celsius: "))
    rea = (celsius * 4)/5
    print("Valor em Réaumur: ", rea)
else:
    print("Escolha invalida.")