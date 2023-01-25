dia = int(input('Digite o dia do mês entre 1 e 30: '))
mes = int(input('Digite o mês entre 1 e 12: '))
dias_pass = (mes * 30) + dia
dias_rest = 365 - dias_pass
if dia < 1 or dia > 30:
    print("Digite o dia correto")
elif mes < 1 or mes > 12:
    print("Digite o mês correto")
else:
    print(f'O dia digitado é {dia} / {mes} \n Já se passaram {dias_pass} dias desse ano \n Restando {dias_rest} para o fim do ano')
