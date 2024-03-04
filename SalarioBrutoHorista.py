ht=float(input("Digitar horas trabalhadas: "))
sh=float(input("Digitar salario hora: "))

#calcular salario bruto
sb=ht*sh

print("\nSalario Bruto: \t", format(sb, "7.2f"))

dap=sb*10/100

print("Desconto Aposentadoria: \t", dap)

si=sb-dap

print("Salario Intermediario: \t", si)

ir=si*5/100

print("Imposto de Renda: \t", ir)

sl=si-ir

print("\nSalario Liquido: \t", sl)