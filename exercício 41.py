#conta = ale + jo + thi
conta = float(input('Digite o valor da conta R$: '))
jo = conta / 3
thi = conta / 3
ale = conta - (jo + thi)
if jo == 0 and thi == 0:
    print(f'O valor pago por Joceir é de R$ {jo:.2f}, \n O valor pago por Thiago é de R$ {thi:.2f}, \n e o valor pago por Alexandre é R$ {ale:.2f}')
else:
    print("Tente novamente")
#print(f'{jo:.2f}')
#print(f'{thi:.2f}')
#print(f'{ale:.2f}')







