anoconstrucao=float(input("Digite o ano construido: "))
anoatual=float(input("Digite o ano atual: "))
iptu=float(input("Digite o IPTU: "))

idade = anoatual - anoconstrucao
if(idade>=40):
    #desconto 30%
    desconto = iptu * 0.3
    resultado = iptu - desconto
    print("\nDesconto de: ", desconto, "\nIPTU com desconto: ", resultado, "\nIdade da casa: ", idade)
elif(idade>=20):
    #desconto 25%
    desconto = iptu * 0.25
    resultado = iptu - desconto
    print("\nDesconto de: ", desconto, "\nIPTU com desconto: ", resultado, "\nIdade da casa: ", idade)
elif(idade>=5):
    #desconto 15%
    desconto = iptu * 0.15
    resultado = iptu - desconto
    print("\nDesconto de: ", desconto, "\nIPTU com desconto: ", resultado, "\nIdade da casa: ", idade)
elif(idade<5):
    print("Nenhum desconto no IPTU. Idade da casa: ", idade)
else:
    print("Idade invalida.")