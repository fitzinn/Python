freq=float(input("Digite a porcentagem de frequencia: "))
aval1=float(input("Digite a nota da avaliação 1: "))
aval2=float(input("Digite a nota da avaliação 2: "))

media = (aval1 + aval2) / 2

if(freq>75):
    if(media>=6):
        print("Aprovado! :D")
    elif(media>=4 and media<6):
        print("Exame.")
    else:
        print("Reprovado. :(")
else:
    print("Reprovado por falta. :(")