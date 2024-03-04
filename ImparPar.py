#ler numero
numero=float(input("Digite o numero: "))

#verificar se impar ou par
resultado = numero % 2
if(resultado == 0):
    print("Seu número é par.")
else:
    print("Seu número é impar.")