try:
    idade=float(input("Digite a sua idade: "))
    if(idade<16):
        print("Não eleitor.")
    elif(idade>=18 and idade<=65):
        print("Eleitor obrigatório.")
    elif(idade>=16 or idade>=65):
        print("Eleitor facultativo.")
except ValueError:
    print("Valor deve ser numerico.")