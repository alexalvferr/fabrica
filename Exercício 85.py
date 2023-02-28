ch_prof1 = int(input('Digite a Quantidade de Horas trabalhadas da Professora 01 durante o mês: '))
ha_prof1 = float(input('Digite o Valor pago da Hora-Aula para a Professora 01: '))
ch_prof2 = int(input('Digite a Quantidade de Horas trabalhadasda Professora 02 durante o mês: '))
ha_prof2 = float(input('Digite o Valor pago da Hora-Aula para a Professora 01: '))
sal_prof1 = ch_prof1 * ha_prof1
sal_prof2 = ch_prof2 * ha_prof2

if sal_prof1 > sal_prof2:
    print(f'O salário da Professora 01 é maior, R$: {sal_prof1:.2f}')
elif sal_prof2 > sal_prof1:
    print(f'O salário da Professora 02 é maior, R$: {sal_prof2:.2f}')
else:
    print(f'Os salários são iguais, R$: {sal_prof2:.2f}')