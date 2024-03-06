import random as r

nc=r.randint(0,100)
acertou = 0
while (acertou==0):
    nj=float(input("Chute um numero: "))
    if(nj < nc):
        print("Numero misterioso é MAIOR do que o chutado.")
    elif(nj > nc):
        print("Numero misterioso é MENOR do que o chutado.")
    elif(nj == nc):
        acertou = 1
        print("Acertou! O numero misterioso era", nc)