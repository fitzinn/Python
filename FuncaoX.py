x=float(input("Digite o valor de x: "))

if(x == 0):
    print("Não é possivel dividir por 0.")
else:
    f=(4 * (x**2) - (3 * x) + 9) / x
    print("Resultado: ", f)