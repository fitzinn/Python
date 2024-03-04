resultado=0
n2=0
op=""

while (True):
    print("OP: ", op, "Resultado: ", resultado, "n2: ", n2)
    d=input(">")
    if((d=="+") or (d=="-") or (d=="*") or (d=="/")):
        if(op!=""):
            if(op=="+"):
                resultado=resultado+n2
                op=""
            elif(op=="-"):
                resultado=resultado-n2
                op=""
            elif(op=="*"):
                resultado=resultado*n2
                op=""
            elif(op=="/"):
                resultado=resultado/n2
                op=""
            n2=resultado
            print(": ", resultado)
        else:
            op=d

    else:
        if(d=="="):
            if(op=="+"):
                resultado=resultado+n2
                op=""
            elif(op=="-"):
                resultado=resultado-n2
                op=""
            elif(op=="*"):
                resultado=resultado*n2
                op=""
            elif(op=="/"):
                resultado=resultado/n2
                op=""
            n2=resultado
            print(": ", resultado)
        else:
            resultado=n2
            n2=float(d)
            