#ler notas
prova1=float(input("Digite a nota da prova 1: "))
prova2=float(input("Digite a nota da prova 2: "))
peso1=float(input("Digite o peso 1: "))
peso2=float(input("Digite o peso 2: "))

#calculo
media = (peso1*prova1 + peso2*prova2) / (peso1 + peso2)

#verificar
if(media>=55 and media<8):
    print("Aprovado!")
elif(media>=8 and media<9):
    print("Parabéns o desempenho foi muito bom!")
elif(media>=9):
    print("Parabéns você foi aprovado com louvor! :D")
else:
    print("Reprovado :(")