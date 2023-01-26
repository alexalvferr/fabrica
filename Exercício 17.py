salario = float(input("Digite o seu seu salário: R$ "))

if salario <= 280:
    percentual = 0.2
elif salario > 280 and salario <= 700:
    percentual = 0.15
elif salario > 700 and salario <= 1500:
    percentual = 0.1
else:
    percentual = 0.05

aumento = salario * (1 + percentual)
salario_final = salario + aumento

print(f"O seu salário atual é de R$ {salario:.2f}")
print(f"O percentual de aumento que você receberá é de {percentual}%")
print(f"O valor de aumento que você receberá é de R$ {aumento:.2f}")
print(f"O seu salário após o aumento será de R$ {salario_final:.2f}")

