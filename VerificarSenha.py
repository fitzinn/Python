#ler senha
senha=float(input("Crie uma senha em numeros: "))

#verificar senha
login=float(input("Insira sua senha: "))
if(login==senha):
    print("Acesso Permitido.")
else:
    print("Acesso Negado.")