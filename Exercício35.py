alcool = 1.9
gas = 2.5

tipo = input('Digite A para abstecer com Álcool ou G para Gasolina: ')
abast = float(input('Digite a quantidade combustível desejada: '))

if tipo == 'A' and abast >= 20:
    print(f'O valor do abastecimento é de: R$ {abast * alcool * 0.95:.2f}')
elif tipo == 'A' and abast < 20:
    print(f'O valor do abastecimento é de: R$ {abast * alcool * 0.97:.2f}')
    
if tipo == 'G' and abast >= 20:
    print(f'O valor do abastecimento é de: R$ {abast * gas * 0.94:.2f}')
elif tipo == 'G' and abast < 20:
    print(f'O valor do abastecimento é de: R$ {abast * gas * 0.96:.2f}') 

else:
    print('Digite uma opção válida')
    
