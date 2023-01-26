valor_hora = float(input("Qual o valor da sua hora trabalhada: R$ "))
horas_trab = float(input("Quantas horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_trab
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
inss = salario_bruto * 0.1

if salario_bruto > 2500:
    percentual = 0.2 * salario_bruto
elif salario_bruto > 1500 and salario_bruto <= 2500:
    percentual = 0.1 * salario_bruto
elif salario_bruto > 900 and salario_bruto <= 1500:
    percentual = 0.05 * salario_bruto
else:
    percentual = 0 * salario_bruto

valor_desc = sindicato + inss + percentual
salario_liq = salario_bruto - valor_desc

print(f"O seu salário bruto é de R$ {salario_bruto:.2f}")
print(f"O desconto do sindicato é de R$ {sindicato:.2f}")
print(f"O desconto do INSS é de R$ {inss:.2f}")
print(f"O desconto do IR é de R$ {percentual:.2f}")
print(f"O valor total descontado é de R$ {valor_desc:.2f}")
print(f"O seu salário líquido é de R$ {salario_liq:.2f}")
print(f"O valor do FGTS depositado pela Empresa é de R$ {fgts:.2f}")



