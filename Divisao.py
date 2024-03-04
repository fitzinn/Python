#ler numeros
n1=float(input("Digite o primeiro numero: "))
n2=float(input("Digite o segundo numero: "))

#fazer conta
if(n2 == 0):
    print("Não é possivel dividir por 0.")
else:
    resultado = n1 % n2
    if(resultado == 0):
        print("É divisivel.")
    else:
        print("Não é divisivel.")